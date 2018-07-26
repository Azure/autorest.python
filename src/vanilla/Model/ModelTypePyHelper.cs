// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.
//
using System.Collections.Generic;
using AutoRest.Core.Model;

namespace AutoRest.Python.Model
{
    /// <remarks>
    /// C# is a strong typed language, and IModelType and Property doesn't respect the same interface.
    /// So declaring twice the same method. We should have an interface to avoid that.
    /// </remarks>
    public static class GenericXmlCtxtSerializer
    {
        public static List<string> XmlSerializationXmlPropCtxt(XmlProperties xmlProperty)
        {
            List<string> combinedXmlDeclarations = new List<string>();

            if(!string.IsNullOrEmpty(xmlProperty.Name))
            {
                combinedXmlDeclarations.Add("'name': '"+xmlProperty.Name+"'");
            }
            if(xmlProperty.Attribute)
            {
                combinedXmlDeclarations.Add("'attr': True");
            }
            if(!string.IsNullOrEmpty(xmlProperty.Prefix))
            {
                combinedXmlDeclarations.Add("'prefix': '"+xmlProperty.Prefix+"'");
            }
            if(!string.IsNullOrEmpty(xmlProperty.Namespace))
            {
                combinedXmlDeclarations.Add("'ns': '"+xmlProperty.Namespace+"'");
            }
            return combinedXmlDeclarations;
        }

        public static List<string> XmlSerializationModelTypeCtxt(IModelType modelProperty)
        {
            List<string> combinedXmlDeclarations = new List<string>();

            if(!string.IsNullOrEmpty(modelProperty.XmlName))
            {
                combinedXmlDeclarations.Add("'name': '"+modelProperty.XmlName+"'");
            }
            if(modelProperty.XmlIsAttribute)
            {
                combinedXmlDeclarations.Add("'attr': True");
            }
            if(!string.IsNullOrEmpty(modelProperty.XmlPrefix))
            {
                combinedXmlDeclarations.Add("'prefix': '"+modelProperty.XmlPrefix+"'");
            }
            if(!string.IsNullOrEmpty(modelProperty.XmlNamespace))
            {
                combinedXmlDeclarations.Add("'ns': '"+modelProperty.XmlNamespace+"'");
            }
            return combinedXmlDeclarations;
        }

        public static List<string> XmlSerializationPropertyCtxt(Property modelProperty)
        {
            List<string> combinedXmlDeclarations = new List<string>();

            if(!string.IsNullOrEmpty(modelProperty.XmlName))
            {
                combinedXmlDeclarations.Add("'name': '"+modelProperty.XmlName+"'");
            }
            if(modelProperty.XmlIsAttribute)
            {
                combinedXmlDeclarations.Add("'attr': True");
            }
            if(!string.IsNullOrEmpty(modelProperty.XmlPrefix))
            {
                combinedXmlDeclarations.Add("'prefix': '"+modelProperty.XmlPrefix+"'");
            }
            if(!string.IsNullOrEmpty(modelProperty.XmlNamespace))
            {
                combinedXmlDeclarations.Add("'ns': '"+modelProperty.XmlNamespace+"'");
            }
            return combinedXmlDeclarations;
        }
    }
}