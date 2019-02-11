// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AutoRest.Core;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;
using AutoRest.Python;
using AutoRest.Python.Model;
using AutoRest.Python.vanilla.Templates;

namespace AutoRest.Python
{
    public class CodeGeneratorPy : CodeGenerator
    {
        private const string ClientRuntimePackage = "msrest version 0.6.0";

        public CodeGeneratorPy()
        {
        }

        public override string UsageInstructions => $"The {ClientRuntimePackage} pip package is required to execute the generated code.";

        public override string ImplementationFileExtension => ".py";

        /// <summary>
        /// Generate Python client code for given ServiceClient.
        /// </summary>
        /// <param name="serviceClient"></param>
        /// <returns></returns>
        public override async Task Generate(CodeModel cm)
        {
            var codeModel = cm as CodeModelPy;
            if (codeModel == null)
            {
                throw new Exception("Code model is not a Python Code Model");
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

            var configurationTemplate = new ConfigurationTemplate { Model = codeModel };
            await Write(configurationTemplate, Path.Combine(folderName, "_configuration.py"));

            var serviceClientTemplate = new ServiceClientTemplate { Model = codeModel };
            await Write(serviceClientTemplate, Path.Combine(folderName, "_" + codeModel.Name.ToPythonCase() + ".py"));

            var serviceClientAsyncTemplate = new ServiceClientTemplateAsync { Model = codeModel };
            await Write(serviceClientAsyncTemplate, Path.Combine(folderName, "_" + codeModel.Name.ToPythonCase() + "_async.py"));

            // If async method at the client level, create another file
            if(codeModel.MethodTemplateModels.Any( each => each.MethodGroup.IsCodeModelMethodGroup))
            {
                var serviceClientOpTemplate = new ServiceClientOperationsTemplate { Model = codeModel };
                await Write(serviceClientOpTemplate, Path.Combine(folderName, "operations", "_" + codeModel.Name.ToPythonCase() + "_operations.py"));

                var serviceClientOpTemplateAsync = new ServiceClientOperationsTemplateAsync { Model = codeModel };
                await Write(serviceClientOpTemplateAsync, Path.Combine(folderName, "operations_async", "_" + codeModel.Name.ToPythonCase() + "_operations_async.py"));
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
            if (codeModel.ModelTypes.Any())
            {
                var modelInitTemplate = new ModelInitTemplate { Model = codeModel };
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

                var methodGroupIndexTemplateAsync = new MethodGroupInitTemplate
                {
                    Model = codeModel,
                    AsyncMode = true
                };
                await Write(methodGroupIndexTemplateAsync, Path.Combine(folderName, "operations_async", "__init__.py"));

                foreach (var methodGroupModel in codeModel.MethodGroupModels)
                {
                    var methodGroupTemplate = new MethodGroupTemplate
                    {
                        Model = methodGroupModel
                    };
                    await Write(methodGroupTemplate, Path.Combine(folderName, "operations", "_" + ((string) methodGroupModel.TypeName).ToPythonCase() + ".py"));
                    // Build a Py3 version that import the Py2 one
                    var methodGroupTemplatePy3 = new MethodGroupTemplateAsync
                    {
                        Model = methodGroupModel
                    };
                    await Write(methodGroupTemplatePy3, Path.Combine(folderName, "operations_async", "_" + ((string) methodGroupModel.TypeName).ToPythonCase() + "_async.py"));
                }
            }

            // Enums
            if (codeModel.EnumTypes.Any())
            {
                var enumTemplate = new EnumTemplate { Model = codeModel.EnumTypes };
                await Write(enumTemplate, Path.Combine(folderName, "models", codeModel.Name.ToPythonCase() + "_enums.py"));
            }
        }

        public async void writeNamespaceFolders(CodeModelPy codeModel)
        {
            if(!codeModel.NoNamespaceFolders)
            {
                string[] namespaceParts = codeModel.Namespace.Split('.');
                for (int i = 1; i < namespaceParts.Length; ++i)
                {
                    string initFolderName = Path.Combine(namespaceParts.Take(i).ToArray());
                    await Write("__import__('pkg_resources').declare_namespace(__name__)",
                                Path.Combine(initFolderName, "__init__.py"), true);
                }
            }
        }

        public static string BuildSummaryAndDescriptionString(string summary, string description)
        {
            StringBuilder builder = new StringBuilder();
            if (!string.IsNullOrEmpty(summary))
            {
                if (!summary.EndsWith(".", StringComparison.OrdinalIgnoreCase))
                {
                    summary += ".";
                }
                builder.AppendLine(summary);
            }

            if (!string.IsNullOrEmpty(summary) && !string.IsNullOrEmpty(description))
            {
                builder.AppendLine(TemplateConstants.EmptyLine);
            }

            if (!string.IsNullOrEmpty(description))
            {
                if (!description.EndsWith(".", StringComparison.OrdinalIgnoreCase))
                {
                    description += ".";
                }
                builder.Append(description);
            }

            return builder.ToString();
        }
    }
}
