// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.
// 

using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using AutoRest.Core;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;
using AutoRest.Extensions;
using AutoRest.Python.Model;
using AutoRest.Python.DAG;
using static AutoRest.Core.Utilities.DependencyInjection;

namespace AutoRest.Python
{
    public class TransformerPy : CodeModelTransformer<CodeModelPy>
    {
        public override CodeModelPy TransformCodeModel(CodeModel cm)
        {
            var codeModel = cm as CodeModelPy;

            // Put the initial namespace value, not transformed by the Core
            // Note that the "Else" is not supposed to be used, since Autorest
            // provides a default value now for Namespace, so Namespace is never empty.
            codeModel.Namespace = Settings.Instance.Namespace.Else(codeModel.Name.ToPythonCase().ToLower());

            // api_version is no longer a parameter of the constructor
            codeModel.Remove(codeModel.Properties.FirstOrDefault(p => p.Name == "api_version"));

            // If one of the constructor parameter is called base_url, rename it to base_url_parameter
            Property baseUrlPRop = codeModel.Properties.FirstOrDefault(each => each.Name == "base_url");
            if(baseUrlPRop != null)
            {
                baseUrlPRop.Name = "base_url_parameter";
            }

            TransformGroupApiVersionToLocal(codeModel);
            SwaggerExtensions.NormalizeClientModel(codeModel);
            PopulateAdditionalProperties(codeModel);
            PopulateDiscriminator(codeModel);
            Flattening(codeModel);
            GenerateConstantProperties(codeModel);

            HashSet<string> touchedNodes = new HashSet<string>();
            List<CompositeTypePy> modelTypeList = new List<CompositeTypePy>();
            
            foreach (var modelType in codeModel.ModelTemplateModels)
            {
                if (!touchedNodes.Contains(modelType.Name) && !string.IsNullOrEmpty(modelType.Name))
                {
                    buildUpDAGNodes(modelType, ref touchedNodes, ref modelTypeList);
                }
            }


            CompositeTypePy rootNode = null;
            DAGraph<CompositeTypePy> dAGraph = null;

            foreach (var modelType in modelTypeList) {
                if (!modelType.hasDependencies() && !string.IsNullOrEmpty(modelType.Name)) {
                    rootNode = modelType;
                    dAGraph = new DAGraph<CompositeTypePy>(rootNode);
                    break;
                }
            }

            foreach (var modelType in modelTypeList)
            {
                if (!modelType.Equals(rootNode))
                {
                    dAGraph.addNode(modelType);
                }
            }
            dAGraph.prepareForEnumeration();
            codeModel.ModelDAGraph = dAGraph;
            return codeModel;
        }

        private CompositeTypePy buildUpDAGNodes(CompositeTypePy modelType, ref HashSet<string> touchedModelTypes, ref List<CompositeTypePy> modelTypeList)
        {
            if (!modelType.HasParent && !string.IsNullOrEmpty(modelType.Name))
            {
                //DAGNode<CompositeType> baseNode = new DAGNode<CompositeType>(modelType.Name);
                modelTypeList.Add(modelType);
                touchedModelTypes.Add(modelType.Name);
                return modelType;
            }
            //DAGNode<CompositeType> curr = new DAGNode<CompositeType>(modelType.Name);
            if (!touchedModelTypes.Contains(modelType.Name) && !string.IsNullOrEmpty(modelType.Name))
            {
                touchedModelTypes.Add(modelType.Name);
                modelType.addDependency(buildUpDAGNodes(modelType.BaseModelType as CompositeTypePy, ref touchedModelTypes, ref modelTypeList).Key);
                modelTypeList.Add(modelType);
            }
            return modelType;
        }

        private void PopulateDiscriminator(CodeModelPy codeModel)
        {
            foreach (var model in codeModel.ModelTypes)
            {
                var compositeTypePy = model as CompositeTypePy;
                if (compositeTypePy != null)
                {
                    compositeTypePy.AddPolymorphicPropertyIfNecessary();
                }
            }
        }

        private void TransformGroupApiVersionToLocal(CodeModelPy codeModel)
        {
            foreach (var methodGroup in codeModel.MethodGroupModels)
            {
                // isClientProperty + ApiVersion will not select anything in Composite mode
                var apiVersionParameters = methodGroup.MethodTemplateModels.SelectMany(x => x.Parameters)
                    .Where(p => p.IsClientProperty && p.SerializedName == "api-version");

                foreach (var apiVersionParameter in apiVersionParameters)
                {
                    apiVersionParameter.Name = "api_version";
                    apiVersionParameter.ClientProperty = null;
                    apiVersionParameter.IsConstant = true;
                    apiVersionParameter.DefaultValue = codeModel.ApiVersion;
                }
            }
        }

        protected void Flattening(CodeModelPy codeModel)
        {
            foreach( var method in codeModel.Methods) { 
            foreach (var parameterTransformation in method.InputParameterTransformation)
            {
                parameterTransformation.OutputParameter.Name = method.GetUniqueName(CodeNamer.Instance.GetParameterName(parameterTransformation.OutputParameter.GetClientName()));

                // QuoteParameter(parameterTransformation.OutputParameter);

                foreach (var parameterMapping in parameterTransformation.ParameterMappings)
                {
                    
                    if (parameterMapping.InputParameterProperty != null)
                    {
                        parameterMapping.InputParameterProperty = CodeNamer.Instance.GetPropertyName(parameterMapping.InputParameterProperty);
                    }

                    if (parameterMapping.OutputParameterProperty != null)
                    {
                        parameterMapping.OutputParameterProperty = CodeNamer.Instance.GetPropertyName(parameterMapping.OutputParameterProperty);
                    }
                }
            }}
        }

        private void GenerateConstantProperties(CodeModelPy codeModel)
        {
            foreach (var methodGroup in codeModel.MethodGroupModels)
            {
                var allParameters = methodGroup.MethodTemplateModels.SelectMany(x => x.Parameters)
                    .Where(p => p.IsConstant && !p.IsClientProperty).ToArray();

                var constantProperties = new List<PropertyPy>();


                foreach (var parameter in allParameters)
                {
                    if (allParameters.Any(p => p.Name == parameter.Name && p.DefaultValue != parameter.DefaultValue))
                    {
                        continue;
                    }

                    if (constantProperties.All(each => each.Name.RawValue != parameter.Name.RawValue))
                    {
                        
                        constantProperties.Add(New<PropertyPy>(new
                        {
                            Name = parameter.Name.RawValue,
                            DefaultValue = parameter.DefaultValue.RawValue,
                            IsConstant = true,
                            IsRequired = parameter.IsRequired,
                            Documentation = parameter.Documentation,
                            SerializedName = parameter.SerializedName,
                            ModelType = parameter.ModelType,
                            IsSpecialConstant = true
                        }));
                    }
                }

                methodGroup.ConstantProperties = constantProperties.Any() ? constantProperties : Enumerable.Empty<PropertyPy>();
            }
        }

        private void PopulateAdditionalProperties(CodeModelPy codeModel)
        {
            if (Settings.Instance.AddCredentials)
            {
                if (!codeModel.Properties.Any(p => Core.Utilities.Extensions.IsPrimaryType(p.ModelType, KnownPrimaryType.Credentials)))
                {
                    codeModel.Add(New<Property>(new
                    {
                        Name = "credentials",
                        SerializedName = "credentials",
                        Type = New<PrimaryType>(KnownPrimaryType.Credentials),
                        IsRequired = true,
                        Documentation = "Subscription credentials which uniquely identify client subscription."
                    }));
                }
            }
        }
    }
}