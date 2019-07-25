// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for license information.

using System;
using AutoRest.Core;
using AutoRest.Core.Utilities;
using AutoRest.Core.Model;
using AutoRest.Python.Model;

namespace AutoRest.Python.Azure.Model
{
    public class PagePya
    {
        private readonly string _typeDefinitionName;

        public PagePya(string className, Property nextLinkProp, Property itemProp, IModelType itemType)
        {
            this._typeDefinitionName = className;
            this.NextLinkProp = nextLinkProp;
            this.ItemProp = itemProp;
            this.ItemType = itemType;
        }

        public Property NextLinkProp { get; private set; }

        public Property ItemProp { get; private set; }

        public string TypeDefinitionName => CodeNamer.Instance.GetTypeName(_typeDefinitionName);

        public IModelType ItemType { get; private set; }

        public string GetReturnTypeDocumentation()
        {
            if((ItemType as CompositeTypePy) == null)
            {
                return ItemType.Name;
            }
            return $":class:`{ItemType.Name} <{((CodeModelPy)ItemType.CodeModel)?.Namespace}.models.{ItemType.Name}>`";
        }
    }
}
