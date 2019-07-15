// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using AutoRest.Core.Model;
using AutoRest.Core;
using AutoRest.Extensions.Azure;
using AutoRest.Python.Model;
using AutoRest.Python.Azure.Model;
using AutoRest.Python.azure.Templates;
using AutoRest.Python.vanilla.Templates;
using System.Collections.Generic;

namespace AutoRest.Python.Azure
{
    public class CodeGeneratorPya : CodeGeneratorPy
    {
        private const string ClientRuntimePackage = "azure-mgmt-core version 0.1.0";

        public override string UsageInstructions => $"The {ClientRuntimePackage} pip package is required to execute the generated code.";

        /// <summary>
        /// Generate Python client code for given ServiceClient.
        /// </summary>
        /// <param name="cm"></param>
        /// <returns></returns>
        public override async Task Generate(CodeModel cm)
        {

            var codeModel = cm as CodeModelPya;
            if (codeModel == null)
            {
                throw new Exception("CodeModel is not a Python Azure Code Model");
            }


            writeNamespaceFolders(codeModel);

            if(codeModel.BasicSetupPy)
            {
                var setupTemplate = new SetupTemplate { Model = codeModel };
                await Write(setupTemplate, "setup.py");
            }

            var noAsync = await Settings.Instance.Host.GetValue<bool?>("no-async");

            var folderName = codeModel.NoNamespaceFolders?"":Path.Combine(codeModel.Namespace.Split('.'));
            var serviceClientInitTemplate = new ServiceClientInitTemplate { Model = codeModel };
            await Write(serviceClientInitTemplate, Path.Combine(folderName, "__init__.py"));

            var configurationTemplate = new AzureConfigurationTemplate { Model = codeModel };
            await Write(configurationTemplate, Path.Combine(folderName, "_configuration.py"));

            // Writing service client
            var serviceClientTemplate = new AzureServiceClientTemplate { Model = codeModel, };
            await Write(serviceClientTemplate, Path.Combine(folderName, "_" + codeModel.Name.ToPythonCase() + ".py"));

            if(codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
            {
                var serviceClientTemplateOp = new AzureServiceClientOperationsTemplate { Model = codeModel };
                await Write(serviceClientTemplateOp, Path.Combine(folderName, "operations", "_" + codeModel.Name.ToPythonCase() + "_operations.py"));
            }

            // do we need to write out the version template file?
            var versionPath = Path.Combine(folderName, "version.py");

            // protect the version file
            await Settings.Instance.Host.ProtectFiles(versionPath);

            if( true != await Settings.Instance.Host.GetValue<bool?>("keep-version-file")  ||  string.IsNullOrEmpty(await Settings.Instance.Host.ReadFile(versionPath)) ) {
                var versionTemplate = new VersionTemplate { Model = codeModel };
                // if they didn't say to keep the old file (or it was not there/empty), write it out.
                await Write(versionTemplate, versionPath);
            }

            //Models
            var models = codeModel.ModelTemplateModels.Where(each => !each.Extensions.ContainsKey(AzureExtensions.ExternalExtension));
            if (models.Any())
            {
                var modelInitTemplate = new AzureModelInitTemplate
                {
                    Model = codeModel
                };
                await Write(modelInitTemplate, Path.Combine(folderName, "models", "__init__.py"));


                var modelTemplate = new ModelTemplate { Model = codeModel.getSortedModels() };
                await Write(modelTemplate, Path.Combine(folderName, "models", "_models.py"));
                modelTemplate.Python3Mode = true;
                await Write(modelTemplate, Path.Combine(folderName, "models", "_models_py3.py"));
            }

            //MethodGroups
            if (codeModel.MethodGroupModels.Any() || codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
            {
                var methodGroupIndexTemplate = new MethodGroupInitTemplate
                {
                    Model = codeModel
                };
                await Write(methodGroupIndexTemplate, Path.Combine(folderName, "operations", "__init__.py"));

                foreach (var methodGroupModel in codeModel.MethodGroupModels)
                {
                    var methodGroupTemplate = new AzureMethodGroupTemplate
                    {
                        Model = methodGroupModel as MethodGroupPya
                    };
                    await Write(methodGroupTemplate, Path.Combine(folderName, "operations", "_" + ((string) methodGroupModel.TypeName).ToPythonCase() + ".py"));
                }
            }

            // Enums
            if (codeModel.EnumTypes.Any())
            {
                var enumTemplate = new EnumTemplate { Model = codeModel.EnumTypes };
                await Write(enumTemplate, Path.Combine(folderName, "models", "_" + codeModel.Name.ToPythonCase() + "_enums.py"));
            }

            // Page class
            if (codeModel.PageModels.Any()) {
                List<PagePya> pagedModels = codeModel.PageModels as List<PagePya>;
                var pageTemplate = new PageTemplate
                {
                    Model = pagedModels
                };
                await Write(pageTemplate, Path.Combine(folderName, "models", "_paged_models.py"));

            }

            // Async
            if (noAsync != true)
            {
                var serviceClientInitTemplateAsync = new ServiceClientInitTemplateAsync { Model = codeModel };
                await Write(serviceClientInitTemplateAsync, Path.Combine(folderName, "aio", "__init__.py"));

                var configurationTemplateAsync = new AzureConfigurationTemplateAsync { Model = codeModel };
                await Write(configurationTemplateAsync, Path.Combine(folderName, "aio", "_configuration_async.py"));

                var serviceClientAsyncTemplate = new AzureServiceClientTemplateAsync { Model = codeModel, };
                await Write(serviceClientAsyncTemplate, Path.Combine(folderName, "aio", "_" + codeModel.Name.ToPythonCase() + "_async.py"));

                if(codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
                {
                    var serviceClientTemplateOpAsync = new AzureServiceClientOperationsTemplateAsync { Model = codeModel };
                    await Write(serviceClientTemplateOpAsync, Path.Combine(folderName, "aio", "operations_async", "_" + codeModel.Name.ToPythonCase() + "_operations_async.py"));
                }

                //MethodGroups
                if (codeModel.MethodGroupModels.Any() || codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
                {
                    var methodGroupIndexTemplateAsync = new MethodGroupInitTemplate
                    {
                        Model = codeModel,
                        AsyncMode = true
                    };
                    await Write(methodGroupIndexTemplateAsync, Path.Combine(folderName, "aio", "operations_async", "__init__.py"));

                    foreach (var methodGroupModel in codeModel.MethodGroupModels)
                    {
                        var methodGroupTemplatePy3 = new AzureMethodGroupTemplateAsync
                        {
                            Model = methodGroupModel as MethodGroupPya
                        };
                        await Write(methodGroupTemplatePy3, Path.Combine(folderName, "aio", "operations_async", "_" + ((string) methodGroupModel.TypeName).ToPythonCase() + "_async.py"));
                    }
                }
            }
        }
    }
}