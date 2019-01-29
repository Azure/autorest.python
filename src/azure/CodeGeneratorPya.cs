// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using AutoRest.Core.Model;
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

            var serviceClientTemplate = new AzureServiceClientTemplate { Model = codeModel, };
            await Write(serviceClientTemplate, Path.Combine(folderName, codeModel.Name.ToPythonCase() + ".py"));

            // If async method at the client level, create another file
            if(codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
            {
                var serviceClientTemplateOp = new AzureServiceClientOperationsTemplate { Model = codeModel };
                await Write(serviceClientTemplateOp, Path.Combine(folderName, "operations", codeModel.Name.ToPythonCase() + "_operations.py"));

                var serviceClientTemplateOpAsync = new AzureServiceClientOperationsTemplateAsync { Model = codeModel };
                await Write(serviceClientTemplateOpAsync, Path.Combine(folderName, "operations", codeModel.Name.ToPythonCase() + "_operations_async.py"));
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
                // var modelTemplate = new ModelTemplate { Model = codeModel.ModelDAGraph };
                // await Write(modelTemplate, Path.Combine(folderName, "models", "_models.py"));
                // modelTemplate.Python3Mode = true;
                // await Write(modelTemplate, Path.Combine(folderName, "models", "_models_py3.py"));
                
                await Write(modelInitTemplate, Path.Combine(folderName, "models", "__init__.py"));

                HashSet<CompositeTypePy> generated_models = new HashSet<CompositeTypePy>();
                List<CompositeTypePy> generate_model_list = new List<CompositeTypePy>();
                foreach(CompositeTypePy model in codeModel.ModelTemplateModels) {
                    if (generated_models.Contains(model)) {
                        continue;
                    }
                    List<CompositeTypePy> ancestors = new List<CompositeTypePy>();
                    CompositeTypePy current = model;
                    ancestors.Add(current);
                    while (current.BaseModelType != null) {
                        CompositeTypePy parent = current.BaseModelType as CompositeTypePy;
                        if (generated_models.Contains(parent)) {
                            break;
                        }
                        ancestors.Insert(0, parent);
                        generated_models.Add(current);
                        current = parent;
                    }
                    generated_models.Add(current);
                    generate_model_list.AddRange(ancestors);
                }
                var modelTemplate = new ModelTemplate { Model = generate_model_list };
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
                    await Write(methodGroupTemplate, Path.Combine(folderName, "operations", ((string) methodGroupModel.TypeName).ToPythonCase() + ".py"));
                    // Build a Py3 version that import the Py2 one
                    var methodGroupTemplatePy3 = new AzureMethodGroupTemplateAsync
                    {
                        Model = methodGroupModel as MethodGroupPya
                    };
                    await Write(methodGroupTemplatePy3, Path.Combine(folderName, "operations", ((string) methodGroupModel.TypeName).ToPythonCase() + "_async.py"));
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
