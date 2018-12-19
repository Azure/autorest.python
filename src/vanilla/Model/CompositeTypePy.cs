﻿// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.Linq;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;
using Newtonsoft.Json;
using static AutoRest.Core.Utilities.DependencyInjection;

namespace AutoRest.Python.Model
{
    public class CompositeTypePy : Core.Model.CompositeType, IExtendedModelTypePy
    {
        private CompositeTypePy _parent => BaseModelType as CompositeTypePy;

        private readonly IList<Core.Model.CompositeType> _subModelTypes = new List<Core.Model.CompositeType>();

        protected CompositeTypePy()
        {
        }

        protected CompositeTypePy(string name) : base(name)
        {
        }

        private IEnumerable<Property> removeDuplicateIfNeeded(IEnumerable<Property> originalEnumerable, IEnumerable<Property> potentialDuplicate)
        {
            if(potentialDuplicate.Count() > 1)
            {
                var potentialDuplicateAsList = potentialDuplicate.ToList();
                var originalEnumerableAsList = originalEnumerable.ToList();
                potentialDuplicateAsList.RemoveAt(0); // Remove randomly one of the list of stuff to remove
                potentialDuplicateAsList.ForEach(delegate(Property prop) {
                    originalEnumerableAsList.Remove(prop);
                });
                return originalEnumerableAsList;
            }
            return originalEnumerable;
        }

        public override IEnumerable<Property> ComposedProperties
        {
            get
            {
                var composed = base.ComposedProperties;

                // Remove duplicate AdditionalProperties from base class
                var addProps = composed.Where(prop => IsAdditionalProperty(prop));
                composed = removeDuplicateIfNeeded(composed, addProps);

                return composed;
            }
        }
        /// <summary>
        /// If PolymorphicDiscriminator is set, makes sure we have a PolymorphicDiscriminator property.
        /// </summary>
        public void AddPolymorphicPropertyIfNecessary()
        {
            if (!string.IsNullOrEmpty(PolymorphicDiscriminator) && Properties.All(p => p.Name != PolymorphicDiscriminator))
            {
                base.Add(New<Property>(new
                {
                    IsRequired = true,
                    Name = PolymorphicDiscriminator,
                    SerializedName = PolymorphicDiscriminator,
                    Documentation = "Constant filled by server.",
                    ModelType = New<PrimaryType>(KnownPrimaryType.String)
                }));
            }
        }

        public IEnumerable<Core.Model.CompositeType> SubModelTypes => BaseIsPolymorphic ? CodeModel.ModelTypes.Where(each => ReferenceEquals(this, each.BaseModelType) ) : Enumerable.Empty<Core.Model.CompositeType>();

        public string SubModelTypeAsString => string.Join(", ", SubModelTypes.Select(x => x.Name));

        public bool IsException => CodeModel.ErrorTypes.Contains(this);

        public bool IsParameterGroup => Properties.All(prop => prop.SerializedName == null);

        public bool IsAdditionalProperty(Property prop)
        {
            return prop.Name.EqualsIgnoreCase("additional_properties") && prop.SerializedName == null && prop.ModelType is DictionaryTypePy;
        }

        public bool HasAdditionalProperty => Properties.Any(prop => IsAdditionalProperty(prop));

        public IList<string> Validators
        {
            get
            {
                List<string> validators = new List<string>();
                foreach (var parameter in ComposedProperties)
                {
                    var validation = new List<string>();
                    if (parameter.IsRequired)
                    {
                        validation.Add("'required': True");
                    }
                    if (parameter.IsConstant)
                    {
                        validation.Add("'constant': True");
                    }
                    if (parameter.IsReadOnly)
                    {
                        validation.Add("'readonly': True");
                    }
                    if (parameter.Constraints.Any())
                    {
                        validation.AddRange(BuildValidationParameters(parameter.Constraints));
                    }
                    if (validation.Any())
                    {
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'{0}': {{{1}}},", parameter.Name, string.Join(", ", validation)));
                    }
                }
                return validators;
            }
        }

        private static List<string> BuildValidationParameters(Dictionary<Constraint, string> constraints)
        {
            List<string> validators = new List<string>();
            foreach (var constraint in constraints.Keys)
            {
                switch (constraint)
                {
                    case Constraint.ExclusiveMaximum:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'maximum_ex': {0}", constraints[constraint]));
                        break;
                    case Constraint.ExclusiveMinimum:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'minimum_ex': {0}", constraints[constraint]));
                        break;
                    case Constraint.InclusiveMaximum:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'maximum': {0}", constraints[constraint]));
                        break;
                    case Constraint.InclusiveMinimum:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'minimum': {0}", constraints[constraint]));
                        break;
                    case Constraint.MaxItems:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'max_items': {0}", constraints[constraint]));
                        break;
                    case Constraint.MaxLength:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'max_length': {0}", constraints[constraint]));
                        break;
                    case Constraint.MinItems:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'min_items': {0}", constraints[constraint]));
                        break;
                    case Constraint.MinLength:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'min_length': {0}", constraints[constraint]));
                        break;
                    case Constraint.MultipleOf:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'multiple': {0}", constraints[constraint]));
                        break;
                    case Constraint.Pattern:
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'pattern': r'{0}'", constraints[constraint]));
                        break;
                    case Constraint.UniqueItems:
                        var pythonBool = Convert.ToBoolean(constraints[constraint], CultureInfo.InvariantCulture) ? "True" : "False";
                        validators.Add(string.Format(CultureInfo.InvariantCulture, "'unique': {0}", pythonBool));
                        break;
                    default:
                        throw new NotSupportedException("Constraint '" + constraint + "' is not supported.");
                }
            }
            return validators;

        }

        public bool HasParent => _parent != null;

        public bool NeedsConstructor
        {
            get
            {
                var nonConstant = Properties.Where(p => !p.IsConstant);
                if (nonConstant.Any())
                {
                    return true;
                }

                return (HasParent || NeedsPolymorphicConverter);
            }
        }

        public string BuildSummaryAndDescriptionString()
        {
            string summaryString = string.IsNullOrWhiteSpace(Summary) &&
                                   string.IsNullOrWhiteSpace(Documentation)
                ? (string)Name
                : Summary;

            return CodeGeneratorPy.BuildSummaryAndDescriptionString(summaryString, Documentation);
        }

        /// <summary>
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
            if (property.IsConstant || property.IsReadOnly)
            {
                docString = string.Format(CultureInfo.InvariantCulture, ":ivar {0}:", property.Name);
            }

            if (property.IsRequired)
            {
                docString += " Required.";
            }

            string summary = property.Summary;
            if (!string.IsNullOrWhiteSpace(summary) && !summary.EndsWith(".", StringComparison.OrdinalIgnoreCase))
            {
                summary += ".";
            }

            string documentation = property.Documentation.Else(string.Empty);
            if (!property.DefaultValue.EqualsIgnoreCase(PythonConstants.None) )
            {
                if (!string.IsNullOrEmpty(documentation) && !documentation.EndsWith(".", StringComparison.OrdinalIgnoreCase))
                {
                    documentation += ".";
                }
                documentation += " Default value: " + property.DefaultValue + " .";
            }

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

        public IList<string> RequiredFieldsList
        {
            get
            {
                List<string> requiredFields = new List<string>();
                foreach (var property in Properties)
                {
                    if (property.IsRequired)
                    {
                        requiredFields.Add(property.Name);
                    }
                }
                if (this._parent != null)
                {
                    requiredFields.AddRange(this._parent.RequiredFieldsList);
                    requiredFields = requiredFields.Distinct().ToList();
                }
                return requiredFields;
            }
        }

        public IEnumerable<Property> ReadOnlyAttributes
        {
            get
            {
                return ComposedProperties.Where(p => p.IsConstant || p.IsReadOnly);
            }
        }

        public IDictionary<string, IModelType> ComplexConstants
        {
            get
            {
                Dictionary<string, IModelType> complexConstant = new Dictionary<string, IModelType> ();
                foreach (var property in Properties)
                {
                    if (property.IsConstant)
                    {
                        Core.Model.CompositeType compType = property.ModelType as Core.Model.CompositeType;
                        if (compType != null)
                        {
                            complexConstant[property.Name] = compType;
                        }
                    }
                }
                return complexConstant;
            }
        }

        /// <remarks>
        /// Used in Python 3, Python 2 doesn't have super signature now.
        /// </remarks>
        public virtual string SuperParameterDeclaration()
        {
            List<string> combinedDeclarations = new List<string>();

            foreach (var property in ComposedProperties.Except(Properties).Except(ReadOnlyAttributes).Where( each =>!each.IsPolymorphicDiscriminator))
            {
                combinedDeclarations.Add(string.Format(CultureInfo.InvariantCulture, "{0}={0}", property.Name));
            }
            combinedDeclarations.Add("**kwargs");
            return string.Join(", ", combinedDeclarations);
        }

        /// <remarks>
        /// Used in Python 3, Python 2 doesn't have typehing * syntax
        /// </remarks>
        public virtual string ModelParameterDeclaration()
        {
            List<string> declarations = new List<string>();
            List<string> requiredDeclarations = new List<string>();
            List<string> combinedDeclarations = new List<string>();

            foreach (var property in ComposedProperties.Except(ReadOnlyAttributes).Where(each => !each.IsPolymorphicDiscriminator))
            {
                if (this.BaseIsPolymorphic)
                    if (property.Name == this.BasePolymorphicDiscriminator)
                        continue;

                string typeHint = ClientModelExtensions.GetPythonTypeHint(property.ModelType) ?? "";
                if(typeHint != "")
                {
                    typeHint = ": " + typeHint;
                }
                if (property.IsRequired && property.DefaultValue.RawValue.IsNullOrEmpty())
                {
                    requiredDeclarations.Add($"{property.Name}{typeHint}");
                }
                else
                {
                    declarations.Add($"{property.Name}{typeHint}={property.DefaultValue}");
                }
            }

            if (requiredDeclarations.Any())
            {
                combinedDeclarations.Add(string.Join(", ", requiredDeclarations));
            }
            if (declarations.Any())
            {
                combinedDeclarations.Add(string.Join(", ", declarations));
            }

            if (!combinedDeclarations.Any())
            {
                return ", **kwargs";
            }
            return ", *, " + string.Join(", ", combinedDeclarations) + ", **kwargs";
        }
        public string SubModelTypeList
        {
            get
            {
                List<string> typeTuple = new List<string>();
                foreach (var modelType in this.SubModelTypes)
                {
                    typeTuple.Add(
                        string.Format(CultureInfo.InvariantCulture, "'{0}': '{1}'",
                            modelType.SerializedName, modelType.Name
                        ));
                }

                return string.Join(", ", typeTuple);
            }
        }

        public virtual string ExceptionTypeDefinitionName
        {
            get
            {
                return this.GetExceptionDefineType();
            }
        }

        public virtual string InitializeProperty(Property modelProperty)
        {
            if (modelProperty == null || modelProperty.ModelType == null)
            {
                throw new ArgumentNullException("modelProperty");
            }

            string xmlDeclarations = "";
            if (CodeModel.ShouldGenerateXmlSerialization)
            {
                List<string> combinedXmlDeclarations = GenericXmlCtxtSerializer.XmlSerializationPropertyCtxt(modelProperty);

                SequenceTypePy sequenceType = modelProperty.ModelType as SequenceTypePy;
                if (sequenceType != null && !string.IsNullOrEmpty(sequenceType.ElementXmlName))
                {
                    combinedXmlDeclarations.AddRange(sequenceType.ItemsSerializationContext());
                }

                xmlDeclarations = string.Format(CultureInfo.InvariantCulture,
                    ", 'xml': {{{1}}}",
                    modelProperty.Name,
                    string.Join(", ", combinedXmlDeclarations)
                );
            }

            //'id':{'key':'id', 'type':'str'},
            return string.Format(CultureInfo.InvariantCulture,
                "'{0}': {{'key': '{1}', 'type': '{2}'{3}}},",
                modelProperty.Name,
                modelProperty.SerializedName,
                ClientModelExtensions.GetPythonSerializationType(modelProperty.ModelType),
                xmlDeclarations
            );
        }

        public virtual string InitializeXmlProperty()
        {
            if(this.XmlProperties == null) {
                return "";
            }
            List<string> combinedXmlDeclarations = GenericXmlCtxtSerializer.XmlSerializationXmlPropCtxt(this.XmlProperties);
            return string.Join(", ", combinedXmlDeclarations);
        }

        public string XmlSerializationCtxt()
        {
            return null;  // CompositeType contains _xml_map, they don't need serialization context
        }

        public string InitializeProperty(string objectName, Property property, bool kwargsMode)
        {
            if (property == null || property.ModelType == null)
            {
                throw new ArgumentNullException("property");
            }
            if (property.IsReadOnly)
            {
                return string.Format(CultureInfo.InvariantCulture, "{0}.{1} = None", objectName, property.Name);
            }
            if (property.IsConstant)
            {
                if (ComplexConstants.ContainsKey(property.Name))
                {
                    return string.Format(CultureInfo.InvariantCulture, "{0} = {1}()", property.Name, property.ModelTypeName);
                }
                else
                {
                    return string.Format(CultureInfo.InvariantCulture, "{0} = {1}", property.Name, property.DefaultValue);
                }
            }
            if (BaseIsPolymorphic && property.IsPolymorphicDiscriminator)
            {
                return string.Format(CultureInfo.InvariantCulture, "{0}.{1} = None", objectName, property.Name);
            }
            if(!kwargsMode)
            {
                return string.Format(CultureInfo.InvariantCulture, "{0}.{1} = {1}", objectName, property.Name);
            }
            else
            {
                if (property.IsRequired && property.DefaultValue.RawValue.IsNullOrEmpty())
                {
                    return string.Format(CultureInfo.InvariantCulture, "{0}.{1} = kwargs.get('{1}', None)", objectName, property.Name);
                }
                return string.Format(CultureInfo.InvariantCulture, "{0}.{1} = kwargs.get('{1}', {2})", objectName, property.Name, property.DefaultValue);
            }
        }

        public bool NeedsPolymorphicConverter => BaseIsPolymorphic && BaseModelType != null;

        /// <summary>
        /// Provides the type of the modelProperty
        /// </summary>
        /// <param name="type">Parameter type to be documented</param>
        /// <returns>Parameter name in the correct jsdoc notation</returns>
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Globalization", "CA1308:NormalizeStringsToUppercase")]
        public string GetPropertyDocumentationType(IModelType type)
        {
            // todo: fix the glitch where some model types don't have their parent reference set correctly
            if (type.Parent == null && (type is CompositeTypePy))
            {
                ((CompositeTypePy)type).CodeModel = CodeModel;
            }
            if (type.Parent == null && (type is EnumTypePy))
            {
                ((EnumTypePy)type).CodeModel = CodeModel;
            }

            return (type as IExtendedModelTypePy)?.TypeDocumentation ?? PythonConstants.None;
        }

        public string TypeDocumentation =>       $"~{((CodeModelPy)CodeModel)?.Namespace}.models.{Name}";
        public string ReturnTypeDocumentation => TypeDocumentation;
    }
}
