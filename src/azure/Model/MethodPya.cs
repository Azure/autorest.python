﻿// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System.Collections.Generic;
using System.Linq;
using System.Net;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;
using AutoRest.Extensions.Azure;
using AutoRest.Python.Model;

namespace AutoRest.Python.Azure.Model
{
    public class MethodPya : MethodPy
    {
        public MethodPya()
        {
        }

        public bool IsPagingMethod => this.Extensions.ContainsKey(AzureExtensions.PageableExtension);

        public string PagingURL { get; set; }

        public IEnumerable<Parameter> PagingParameters { get; set; }

        public IModelType PagedResponseClass
        {
            get
            {
                var ext = this.Extensions[AzureExtensions.PageableExtension] as Newtonsoft.Json.Linq.JContainer;
                if (ext == null)
                {
                    return null;
                }

                return this.ReturnType.Body;
            }
        }

        public IModelType PagedResponseContentClass { get; set; }

        public string ClientRequestIdString => AzureExtensions.GetClientRequestIdString(this);

        public string RequestIdString => AzureExtensions.GetRequestIdString(this);

        /// <summary>
        /// Returns true if method has x-ms-long-running-operation extension.
        /// </summary>
        public bool IsLongRunningOperation
        {
            get { return Extensions.ContainsKey(AzureExtensions.LongRunningExtension); }
        }

        public bool HasCloudError => ((CodeModelPya)CodeModel).AzureArm && (DefaultResponse.Body == null || DefaultResponse.Body.Name == "CloudError");

        public bool HasHttpResponseError => !((CodeModelPya)CodeModel).AzureArm && DefaultResponse.Body == null;

        public override string ExceptionDocumentation
        {
            get
            {
                if (HasHttpResponseError)
                {
                    return ":class:`HttpResponseError<azure.core.HttpResponseError>`";
                }
                else if(HasCloudError)
                {
                    return ":class:`ARMError<azure.mgmt.core.ARMError>`";
                }
                return base.ExceptionDocumentation;
            }
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "exp"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "HttpResponseError")]
        public override string RaisedException
        {
            get
            {
                if (HasHttpResponseError)
                {
                    var sb = new IndentedStringBuilder();
                    sb.AppendLine("map_error(status_code=response.status_code, response=response, error_map=error_map)");
                    sb.AppendLine("raise HttpResponseError(response=response)");
                    return sb.ToString();
                }
                if (HasCloudError)
                {
                    var sb = new IndentedStringBuilder();
                    sb.AppendLine("map_error(status_code=response.status_code, response=response, error_map=error_map)");
                    sb.AppendLine("raise ARMError(response=response)");
                    return sb.ToString();
                }

                return base.RaisedException;
            }
        }

        /// <summary>
        /// Gets the expression for default header setting.
        /// </summary>
        public override string SetDefaultHeaders
        {
            get
            {
                var sb = new IndentedStringBuilder();
                sb.AppendLine("if self._config.generate_client_request_id:", this.ClientRequestIdString).Indent();
                sb.AppendLine("header_parameters['{0}'] = str(uuid.uuid1())", this.ClientRequestIdString).Outdent().Append(base.SetDefaultHeaders);
                return sb.ToString();
            }
        }

        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Naming", "CA2204:Literals should be spelled correctly", MessageId = "addheaders"), System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1303:Do not pass literals as localized parameters", MessageId = "AutoRest.Core.Utilities.IndentedStringBuilder.AppendLine(System.String)")]
        public override string ReturnEmptyResponse
        {
            get
            {
                if (this.HttpMethod == HttpMethod.Head && this.ReturnType.Body.IsPrimaryType(KnownPrimaryType.Boolean))
                {
                    HttpStatusCode code = this.Responses.Keys.FirstOrDefault(AzureExtensions.HttpHeadStatusCodeSuccessFunc);
                    var builder = new IndentedStringBuilder("    ");
                    builder.AppendFormat("deserialized = (response.status_code == {0})", (int)code).AppendLine();
                    builder.AppendLine("return deserialized");

                    return builder.ToString();
                }
                else
                {
                    return base.ReturnEmptyResponse;
                }
            }
        }

        public string GetLROOptions()
        {
            // Do this only for POST with return type for now
            if(HttpMethod != HttpMethod.Post || ReturnType == null)
            {
                return "";
            }
            string finalLroString = "";
            switch (LongRunningFinalState)
            {
                case FinalStateVia.Location:
                    finalLroString = "location";
                    break;
                case FinalStateVia.AzureAsyncOperation:
                    finalLroString = "azure-async-operation";
                    break;
                default:
                    break;
            }
            if(finalLroString != "")
            {
                return "{'final-state-via': '"+finalLroString+"'}";
            }
            return "";
        }
    }
}