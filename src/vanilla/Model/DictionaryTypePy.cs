// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.
// 

using AutoRest.Core.Model;

namespace AutoRest.Python.Model
{
    public class DictionaryTypePy : DictionaryType, IExtendedModelTypePy
    {
        public DictionaryTypePy()
        {
            Name.OnGet += v => $"dict";
        }

        public string TypeDocumentation => $"dict[str, {((IExtendedModelTypePy)ValueType).TypeDocumentation}]";
        public string ReturnTypeDocumentation => TypeDocumentation;
    }

}