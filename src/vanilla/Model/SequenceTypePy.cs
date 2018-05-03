// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.
// 
using System.Collections.Generic;
using AutoRest.Core.Model;

namespace AutoRest.Python.Model
{
    public class SequenceTypePy : SequenceType, IExtendedModelTypePy
    {
        public SequenceTypePy()
        {
            Name.OnGet += v => $"list";
        }

        public string TypeDocumentation => $"list[{((IExtendedModelTypePy)ElementType).TypeDocumentation}]";
        public string ReturnTypeDocumentation => TypeDocumentation;


        public List<string> ItemsSerializationContext()
        {
            List<string> combinedXmlDeclarations = new List<string>();

            combinedXmlDeclarations.Add("'itemsName': '"+ElementXmlName+"'");
            if(XmlIsWrapped)
            {
                combinedXmlDeclarations.Add("'wrapped': True");
            }            
            if(!string.IsNullOrEmpty(ElementXmlPrefix))
            {
                combinedXmlDeclarations.Add("'itemsPrefix': '"+ElementXmlPrefix+"'");
            }
            if(!string.IsNullOrEmpty(ElementXmlNamespace))
            {
                combinedXmlDeclarations.Add("'itemsNs': '"+ElementXmlNamespace+"'");
            }            
            return combinedXmlDeclarations;
        }
        public string XmlSerializationCtxt()
        {
            List<string> combinedXmlDeclarations = GenericXmlCtxtSerializer.XmlSerializationModelTypeCtxt(this);
            combinedXmlDeclarations.AddRange(ItemsSerializationContext());

            return string.Format(
                "{{{0}}}",
                string.Join(", ", combinedXmlDeclarations)
            );
        }        
    }
}