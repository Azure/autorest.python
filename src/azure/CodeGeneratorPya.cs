// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using AutoRest.Core.Model;
using AutoRest.Extensions.Azure;
using AutoRest.Python.Azure.Model;
using AutoRest.Python.azure.Templates;
using AutoRest.Python.vanilla.Templates;

namespace AutoRest.Python.Azure
{
    public class CodeGeneratorPya : CodeGeneratorPy
    {
        private const string ClientRuntimePackage = "msrestazure version 0.6.0";

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

            var folderName = codeModel.NoNamespaceFolders?"":Path.Combine(codeModel.Namespace.Split('.'));
            var serviceClientInitTemplate = new ServiceClientInitTemplate { Model = codeModel };
            await Write(serviceClientInitTemplate, Path.Combine(folderName, "__init__.py"));

            var configurationTemplate = new AzureConfigurationTemplate { Model = codeModel };
            await Write(configurationTemplate, Path.Combine(folderName, "_configuration.py"));

            var serviceClientInitTemplateAsync = new ServiceClientInitTemplateAsync { Model = codeModel };
            await Write(serviceClientInitTemplateAsync, Path.Combine(folderName, "aio", "__init__.py"));

            // Writing service client
            var serviceClientTemplate = new AzureServiceClientTemplate { Model = codeModel, };
            await Write(serviceClientTemplate, Path.Combine(folderName, "_" + codeModel.Name.ToPythonCase() + ".py"));

            var serviceClientAsyncTemplate = new AzureServiceClientTemplateAsync { Model = codeModel, };
            await Write(serviceClientAsyncTemplate, Path.Combine(folderName, "aio", "_" + codeModel.Name.ToPythonCase() + "_async.py"));

            // If async method at the client level, create another file
            if(codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
            {
                var serviceClientTemplateOp = new AzureServiceClientOperationsTemplate { Model = codeModel };
                await Write(serviceClientTemplateOp, Path.Combine(folderName, "operations", "_" + codeModel.Name.ToPythonCase() + "_operations.py"));

                var serviceClientTemplateOpAsync = new AzureServiceClientOperationsTemplateAsync { Model = codeModel };
                await Write(serviceClientTemplateOpAsync, Path.Combine(folderName, "aio", "operations_async", "_" + codeModel.Name.ToPythonCase() + "_operations_async.py"));
            }

            var versionTemplate = new VersionTemplate { Model = codeModel, };
            await Write(versionTemplate, Path.Combine(folderName, "version.py"));

            //Models
            var models = codeModel.ModelTemplateModels.Where(each => !each.Extensions.ContainsKey(AzureExtensions.ExternalExtension));
            if (models.Any())
            {
                var modelInitTemplate = new AzureModelInitTemplate
                {
                    Model = codeModel
                };
                await Write(modelInitTemplate, Path.Combine(folderName, "models", "__init__.py"));

                foreach (var modelType in models)
                {
                    var modelTemplate = new ModelTemplate { Model = modelType };
                    await Write(modelTemplate, Path.Combine(folderName, "models", modelType.Name.ToPythonCase() + ".py"));
                    // Rebuild the same in Python 3 mode
                    modelTemplate.Python3Mode = true;
                    await Write(modelTemplate, Path.Combine(folderName, "models", modelType.Name.ToPythonCase() + "_py3.py"));
                }
            }

            //MethodGroups
            if (codeModel.MethodGroupModels.Any() || codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
            {
                var methodGroupIndexTemplate = new MethodGroupInitTemplate
                {
                    Model = codeModel
                };
                await Write(methodGroupIndexTemplate, Path.Combine(folderName, "operations", "__init__.py"));

                var methodGroupIndexTemplateAsync = new MethodGroupInitTemplate
                {
                    Model = codeModel,
                    AsyncMode = true
                };
                await Write(methodGroupIndexTemplateAsync, Path.Combine(folderName, "aio", "operations_async", "__init__.py"));

                foreach (var methodGroupModel in codeModel.MethodGroupModels)
                {
                    var methodGroupTemplate = new AzureMethodGroupTemplate
                    {
                        Model = methodGroupModel as MethodGroupPya
                    };
                    await Write(methodGroupTemplate, Path.Combine(folderName, "operations", "_" + ((string) methodGroupModel.TypeName).ToPythonCase() + ".py"));
                    // Build a Py3 version that import the Py2 one
                    var methodGroupTemplatePy3 = new AzureMethodGroupTemplateAsync
                    {
                        Model = methodGroupModel as MethodGroupPya
                    };
                    await Write(methodGroupTemplatePy3, Path.Combine(folderName, "aio", "operations_async", "_" + ((string) methodGroupModel.TypeName).ToPythonCase() + "_async.py"));
                }
            }

            // Enums
            if (codeModel.EnumTypes.Any())
            {
                var enumTemplate = new EnumTemplate { Model = codeModel.EnumTypes };
                await Write(enumTemplate, Path.Combine(folderName, "models", codeModel.Name.ToPythonCase() + "_enums.py"));
            }

            // Page class
            foreach (var pageModel in codeModel.PageModels)
            {
                var pageTemplate = new PageTemplate
                {
                    Model = pageModel
                };
                await Write(pageTemplate, Path.Combine(folderName, "models", pageModel.TypeDefinitionName.ToPythonCase() + ".py"));
            }
        }
    }
}
