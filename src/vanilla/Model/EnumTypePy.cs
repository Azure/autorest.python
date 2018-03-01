﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AutoRest.Core.Model;
using AutoRest.Core.Utilities;

namespace AutoRest.Python.Model
{
    public class EnumTypePy : EnumType, IExtendedModelTypePy
    {
        public string TypeDocumentation => Parent == null || Name.IsNullOrEmpty() ? "str" : $"str or ~{((CodeModelPy)CodeModel)?.Namespace}.models.{Name}";
        //ModelAsString ? 
        //"str" : 
        public string ReturnTypeDocumentation => ModelAsString || Parent == null ? "str" :  $"~{((CodeModelPy)CodeModel)?.Namespace}.models.{Name}";
    }
}
