﻿// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Runtime.CompilerServices;
using AutoRest.Core;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;
using AutoRest.Extensions;
using Newtonsoft.Json;

namespace AutoRest.Python.Model
{
    public class CodeModelPy : CodeModel
    {
        public CodeModelPy()
        {
            // todo: properties is expected to be just the non-constant properties.
            // Properties.RemoveAll(p => ConstantProperties.Contains(p));
        }

        [JsonIgnore]
        public bool IsCustomBaseUri => Extensions.ContainsKey(SwaggerExtensions.ParameterizedHostExtension);

        [JsonIgnore]
        public IEnumerable<Property> ConstantProperties => Properties.Where(p => p.IsConstant);

        [JsonIgnore]
        public IEnumerable<MethodPy> MethodTemplateModels => Methods.Cast<MethodPy>();

        [JsonIgnore]
        public IEnumerable<CompositeTypePy> ModelTemplateModels => ModelTypes.Cast<CompositeTypePy>();

        [JsonIgnore]
        public virtual IEnumerable<MethodGroupPy> MethodGroupModels => Operations.Cast<MethodGroupPy>().Where( each => !each.IsCodeModelMethodGroup);
        

        public string PolymorphicDictionary
        {
            get
            {
                IndentedStringBuilder builder = new IndentedStringBuilder(IndentedStringBuilder.TwoSpaces);
                var polymorphicTypes = ModelTemplateModels.Where(m => m.BaseIsPolymorphic);

                for (int i = 0; i < polymorphicTypes.Count(); i++ )
                {
                    builder.Append(string.Format(CultureInfo.InvariantCulture, 
                        "'{0}' : exports.{1}",
                            polymorphicTypes.ElementAt(i).SerializedName, 
                            polymorphicTypes.ElementAt(i).Name));

                    if(i == polymorphicTypes.Count() -1)
                    {
                        builder.AppendLine();
                    }
                    else 
                    {
                        builder.AppendLine(",");
                    }
                }
                
                return builder.ToString();
            }
        }

        public virtual string RequiredConstructorParameters
        {
            get
            {
                var parameters = this.Properties.Where( each => !each.IsConstant).OrderBy(item => !item.IsRequired);
                var requireParams = new List<string>();
                foreach (var property in parameters)
                {
                    if (property.IsConstant)
                    {
                        continue;
                    }
                    if (property.IsRequired)
                    {
                        requireParams.Add(property.Name);
                    }
                    else
                    {
                        requireParams.Add(string.Format(CultureInfo.InvariantCulture, "{0}=None", property.Name));
                    }
                }
                //requireParams.Add("baseUri");
                var param = string.Join(", ", requireParams);
                if (!string.IsNullOrEmpty(param))
                {
                    param = ", " + param;
                }
                return param;
            }
        }

        public virtual string ConfigConstructorParameters
        {
            get
            {
                var parameters = this.Properties.Where(each => !each.IsConstant).OrderBy(item => !item.IsRequired);
                var configParams = new List<string>();
                foreach (var property in parameters)
                {
                    configParams.Add(property.Name);
                }
                var param = string.Join(", ", configParams);
                if (!IsCustomBaseUri)
                {
                    param += (param.IsNullOrEmpty() ? "" : ", ") + "base_url";
                }
                return param;
            }
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "ValueError"),
            System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "TypeError"),
            System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "str"),
            System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)")]
        public virtual string ValidateRequiredParameters
        {
            get
            {
                var builder = new IndentedStringBuilder("    ");
                foreach (var property in this.Properties.Where( each => !each.IsConstant ))
                {
                    if (property.IsRequired)
                    {
                        builder.
                            AppendFormat("if {0} is None:", property.Name).AppendLine().
                            Indent().
                                AppendLine(string.Format(CultureInfo.InvariantCulture, "raise ValueError(\"Parameter '{0}' must not be None.\")", property.Name)).
                            Outdent();
                    }
                }
                return builder.ToString();
            }
        }

        public virtual string UserAgent => PackageName;

        public virtual string SetupRequires => @"""msrest>=0.2.0""";
        

        public string Version => Settings.Instance.PackageVersion.Else(ApiVersion);

        public bool ClientSideValidationEnabled => (bool)Settings.Instance.CustomSettings["ClientSideValidation"];

        public virtual bool HasAnyModel => ModelTemplateModels.Any();

        public string PackageName => Settings.Instance.PackageName.Else(Name.ToPythonCase().Replace("_", ""));

        private string _namespace;
        public override string Namespace
        {
            get { return _namespace; }
            set
            {
                if (value != _namespace)
                {
                    // In Python, the Autorest Code normalisation is not good.
                    // So we change the setter to keep the value
                    // and we put the initial Namespace value back from the Python
                    // transformer.
                    // We lower it to respect PEP8
                    _namespace = value.ToLower();
                }
            }
        }

        public string ServiceDocument
        {
            get
            {
                if (string.IsNullOrWhiteSpace(this.Documentation))
                {
                    return this.Name;
                }
                else
                {
                    return this.Documentation.EscapeXmlComment();
                }
            }
        }

        /// Provides the modelProperty documentation string along with default value if any.
        /// </summary>
        /// <param name="property">Parameter to be documented</param>
        /// <returns>Parameter documentation string along with default value if any 
        /// in correct jsdoc notation</returns>
        public static string GetPropertyDocumentationString(Property property)
        {
            if (property == null)
            {
                throw new ArgumentNullException("property");
            }
            string docString = string.Format(CultureInfo.InvariantCulture, ":param {0}:", property.Name);
            if (property.IsConstant)
            {
                docString = string.Format(CultureInfo.InvariantCulture, ":ivar {0}:", property.Name);
            }

            string summary = property.Summary;
            if (!string.IsNullOrWhiteSpace(summary) && !summary.EndsWith(".", StringComparison.OrdinalIgnoreCase))
            {
                summary += ".";
            }

            string documentation = property.Documentation;
            if (!string.IsNullOrWhiteSpace(summary))
            {
                docString += " " + summary;
            }

            if (!string.IsNullOrWhiteSpace(documentation))
            {
                docString += " " + documentation;
            }
            return docString;
        }

        /// <summary>
        /// Provides the type of the modelProperty
        /// </summary>
        /// <param name="type">Parameter type to be documented</param>
        /// <returns>Parameter name in the correct jsdoc notation</returns>
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase")]
        public string GetPropertyDocumentationType(IModelType type)
        {
            return (type as IExtendedModelTypePy)?.TypeDocumentation ?? PythonConstants.None;
        }

        public virtual bool NeedsExtraImport => false;

        public bool HasAnyDefaultExceptions => MethodTemplateModels.Any(item => item.DefaultResponse.Body == null);

        public bool HasAnyDeprecated => this.MethodTemplateModels.Any(item => item.Deprecated);

        public virtual string GetExceptionNameIfExist(IModelType type, bool needsQuote)
        {
            CompositeType compType = type as CompositeType;
            if (compType != null)
            {
                if (ErrorTypes.Contains(compType))
                {
                    if (needsQuote)
                    {
                        return ", '" + compType.GetExceptionDefineType() + "'";
                    }
                    return ", " + compType.GetExceptionDefineType();
                }
            }

            return string.Empty;
        }
    }
}