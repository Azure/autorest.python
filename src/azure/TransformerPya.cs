// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.
// 

using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Linq;
using AutoRest.Core;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;
using AutoRest.Extensions;
using AutoRest.Extensions.Azure;
using AutoRest.Python.Azure.Model;
using Newtonsoft.Json.Linq;
using static AutoRest.Core.Utilities.DependencyInjection;

namespace AutoRest.Python.Azure
{
    public class TransformerPya : CodeModelTransformer<CodeModelPya, TransformerPy>
    {
        public override CodeModelPya TransformCodeModel(CodeModel cm)
        {
            var codeModel = (CodeModelPya)cm;
            TransformPagingMethods(codeModel);
            // Don't add pagable/longrunning method since we already handle ourself.
            Settings.Instance.AddCredentials = true;

            AzureExtensions.ProcessClientRequestIdExtension(codeModel);
            AzureExtensions.UpdateHeadMethods(codeModel);
            AzureExtensions.ParseODataExtension(codeModel);
            SwaggerExtensions.FlattenModels(codeModel);
            ParameterGroupExtensionHelper.AddParameterGroups(codeModel);
            AddAzureProperties(codeModel);
            AzureExtensions.SetDefaultResponses(codeModel);
            CorrectFilterParameters(codeModel);

            Base.TransformCodeModel(codeModel);
            
            NormalizePaginatedMethods(codeModel);

            return codeModel;
        }

        private void TransformPagingMethods(CodeModelPya codeModel)
        {
            foreach (var methodGroup in codeModel.Operations)
            {
                // methods in this group that have a pageable extension
                var current = methodGroup.Methods.Where(m => m.Extensions.ContainsKey(AzureExtensions.PageableExtension)).ToArray();

                foreach (MethodPya method in current)
                {
                    var pageableExtension =
                        method.Extensions[AzureExtensions.PageableExtension] as Newtonsoft.Json.Linq.JContainer;

                    /* We don't support LRO + Paging at the same time for now */
                    if (method.Extensions.ContainsKey(AzureExtensions.LongRunningExtension))
                    {
                        method.Extensions.Remove(AzureExtensions.PageableExtension);
                        continue;
                    }

                    var operationName = (string) pageableExtension["operationName"];
                    if (operationName != null)
                    {
                        var nextLinkMethod =
                            methodGroup.Methods.FirstOrDefault(m => operationName.EqualsIgnoreCase(m.SerializedName));
                        if (nextLinkMethod != null)
                        {
                            // set the nextlink settings for the method 
                            method.PagingURL = nextLinkMethod.Url;
                            method.PagingParameters = nextLinkMethod.LogicalParameters;

                            // removes the nextlink method.
                            methodGroup.Remove(nextLinkMethod);
                        }
                    }
                }
            }
        }

        [SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "nextLink")]
        private string GetPagingSetting(CodeModelPya codeModel, CompositeType body, Dictionary<string, object> extensions, IModelType valueType,
            IDictionary<int, string> typePageClasses, string methodName)
        {
            string valueTypeName = valueType.Name;
            var ext = extensions[AzureExtensions.PageableExtension] as JContainer;

            var ignoreNextLink = false;
            if ((ext["nextLinkName"] != null) && (ext["nextLinkName"].Type == JTokenType.Null))
            {
                ignoreNextLink = true;
            }
            var nextLinkName = (string) ext["nextLinkName"] ?? "nextLink";
            var itemName = (string) ext["itemName"] ?? "value";

            // nextLinkName = nextLinkName.Replace(".", "\\\\.");
            // itemName = itemName.Replace(".", "\\\\.");
            var findNextLink = false;
            var findItem = false;
            foreach (var property in body.ComposedProperties)
            {
                var propName = property.SerializedName;

                if (propName == nextLinkName)
                {
                    findNextLink = true;
                    nextLinkName = property.SerializedName = property.SerializedName.Replace(".", "\\\\.")?.Replace("\\\\\\\\", "\\\\");

                }
                else if (propName == itemName)
                {
                    findItem = true;
                    itemName = property.SerializedName = property.SerializedName.Replace(".", "\\\\.")?.Replace("\\\\\\\\", "\\\\");
                }

                if (propName == nextLinkName.Replace(".", "\\\\.")?.Replace("\\\\\\\\", "\\\\"))
                {
                    nextLinkName = nextLinkName.Replace(".", "\\\\.")?.Replace("\\\\\\\\", "\\\\");
                    findNextLink = true;
                }
                else if (propName == itemName.Replace(".", "\\\\.")?.Replace("\\\\\\\\", "\\\\"))
                {
                    itemName = itemName.Replace(".", "\\\\.")?.Replace("\\\\\\\\", "\\\\");
                    findItem = true;
                }
            }

            if (!findItem)
            {
                throw new KeyNotFoundException("Couldn't find the item property specified by extension");
            }

            string className;
            var hash = (nextLinkName + "#" + itemName).GetHashCode();
            if (!typePageClasses.ContainsKey(hash))
            {
                className = (string) ext["className"];
                if (string.IsNullOrEmpty(className))
                {
                    if (typePageClasses.Count > 0)
                    {
                        className = valueTypeName +
                                    string.Format(CultureInfo.InvariantCulture, "Paged{0}", typePageClasses.Count);
                    }
                    else
                    {
                        className = valueTypeName + "Paged";
                    }
                }
                typePageClasses.Add(hash, className);
            }

            className = typePageClasses[hash];
            ext["className"] = className;

            var pageModel = new PagePya(className, nextLinkName, itemName, valueType);
            if (!codeModel.PageModels.Contains(pageModel))
            {
                codeModel.PageModels.Add(pageModel);
            }

            return className;
        }

        /// <summary>
        ///     Changes paginated method signatures to return Page type.
        /// </summary>
        /// <param name="codeModel"></param>
        private void NormalizePaginatedMethods(CodeModelPya codeModel)
        {
            if (codeModel == null)
            {
                throw new ArgumentNullException("codeModel");
            }

            var convertedTypes = new Dictionary<IModelType, Response>();

            foreach (MethodPya method in codeModel.Methods.Where(m => m is MethodPya && m.Extensions.ContainsKey(AzureExtensions.PageableExtension)))
            {
                foreach (var responseStatus in method.Responses.Where(r => r.Value.Body is CompositeType).Select(s => s.Key))
                {
                    var compositType = (CompositeType) method.Responses[responseStatus].Body;
                    var sequenceType = compositType.Properties.Select(p => p.ModelType).FirstOrDefault(t => t is SequenceType) as SequenceType;

                    // if the type is a wrapper over page-able response
                    if (sequenceType != null)
                    {
                        var valueType = sequenceType.ElementType;
                        string valueTypeName = valueType.Name;
                        if (!codeModel.PageClasses.ContainsKey(valueTypeName))
                        {
                            codeModel.PageClasses.Add(valueTypeName, new Dictionary<int, string>());
                        }
                        var pagableTypeName = GetPagingSetting(codeModel, compositType, method.Extensions, valueType,
                            codeModel.PageClasses[valueTypeName], method.SerializedName);

                        var pagedResult = New<CompositeType>(pagableTypeName);
                        
                        // make sure the parent reference is set.
                        pagedResult.CodeModel = codeModel;

                        method.PagedResponseContentClass = valueType; // Save the content type model

                        convertedTypes[compositType] = new Response(pagedResult, null);
                        method.Responses[responseStatus] = convertedTypes[compositType];
                        break;
                    }
                }

                if (convertedTypes.ContainsKey(method.ReturnType.Body))
                {
                    method.ReturnType = convertedTypes[method.ReturnType.Body];
                }
            }

            SwaggerExtensions.RemoveUnreferencedTypes(codeModel, new HashSet<string>(convertedTypes.Keys.Cast<CompositeType>().Select(t => t.Name.Value)));
        }

        /// <summary>
        ///     Corrects type of the filter parameter. Currently typization of filters isn't
        ///     supported and therefore we provide to user an opportunity to pass it in form
        ///     of raw string.
        /// </summary>
        /// <param name="serviceClient">The service client.</param>
        public static void CorrectFilterParameters(CodeModel serviceClient)
        {
            if (serviceClient == null)
            {
                throw new ArgumentNullException("serviceClient");
            }

            foreach (
                var method in serviceClient.Methods.Where(m => m.Extensions.ContainsKey(AzureExtensions.ODataExtension))
            )
            {
                var filterParameter = method.Parameters.FirstOrDefault(p =>
                    p.SerializedName.EqualsIgnoreCase("$filter") &&
                    (p.Location == ParameterLocation.Query) &&
                    p.ModelType is CompositeType);

                if (filterParameter != null)
                {
                    filterParameter.ModelType = New<PrimaryType>(KnownPrimaryType.String);
                }
            }
        }

        /// <summary>
        /// Creates azure specific properties.
        /// </summary>
        /// <param name="codeModelient"></param>
        private static void AddAzureProperties(CodeModel codeModel)
        {
            var acceptLanguage = codeModel.Properties
                .FirstOrDefault(p => AzureExtensions.AcceptLanguage.EqualsIgnoreCase(p.SerializedName));

            AzureExtensions.AddAzureProperties(codeModel);
            codeModel.Remove(codeModel.Properties.FirstOrDefault(p => p.Name == "long_running_operation_retry_timeout"));
            codeModel.Remove(codeModel.Properties.FirstOrDefault(p => p.Name == "generate_client_request_id"));
            codeModel.Remove(codeModel.Properties.FirstOrDefault(p => p.Name == "accept_language"));

            if (acceptLanguage != null) // && acceptLanguage.DefaultValue != "en-US"
            {
                acceptLanguage.IsReadOnly = true;
                acceptLanguage.IsRequired = false;
                acceptLanguage.ModelType = New<PrimaryType>(KnownPrimaryType.String);
                codeModel.Add(acceptLanguage);
            }
        }
    }
}