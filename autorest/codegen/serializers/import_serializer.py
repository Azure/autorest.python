# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from copy import deepcopy
from typing import List
from ..models.imports import ImportType, FileImport, ImportModel, TypingSection, TypeDefinition

def _serialize_package(
    imports: List[ImportModel], delimiter: str
) -> str:
    buffer = []
    if any(i for i in imports if i.submodule_name is None):
        buffer.append(f"import {imports[0].module_name}{f' as {imports[0].alias}' if imports[0].alias else ''}")
    else:
        import_str = ", ".join(sorted([
            f"{i.submodule_name} as {i.alias}" if i.alias else i.submodule_name for i in imports # type: ignore
        ]))
        buffer.append(f"from {imports[0].module_name} import {import_str}")
    return delimiter.join(buffer)

def _serialize_import_type(imports: List[ImportModel], delimiter: str) -> str:
    """Serialize a given import type."""
    import_list = []
    for module_name in sorted(set(i.module_name for i in imports)):

        import_list.append(_serialize_package([
            i for i in imports if i.module_name == module_name
        ], delimiter))
    return delimiter.join(import_list)

def _get_import_clauses(
    imports: List[ImportModel], delimiter: str
) -> List[str]:
    import_clause = []
    for import_type in ImportType:
        imports_with_import_type = [i for i in imports if i.import_type == import_type]
        if imports_with_import_type:
            import_clause.append(_serialize_import_type(imports_with_import_type, delimiter))
    return import_clause


class FileImportSerializer:
    def __init__(self, file_import: FileImport, is_python3_file: bool, async_mode: bool = False) -> None:
        self.file_import = file_import
        self.is_python3_file = is_python3_file
        self.async_mode = async_mode

    def _get_imports_list(self, baseline_typing_section: TypingSection, add_conditional_typing: bool):
        # If this is a python 3 file, our regular imports include the CONDITIONAL category
        # If this is not a python 3 file, our typing imports include the CONDITIONAL category
        file_import_copy = deepcopy(self.file_import)
        if add_conditional_typing and any(
            self.file_import.get_imports_from_section(TypingSection.CONDITIONAL)
        ):
            # we switch the TypingSection key for the CONDITIONAL typing imports so we can merge
            # the imports together
            for i in file_import_copy.imports:
                if i.typing_section == TypingSection.CONDITIONAL:
                    i.typing_section = baseline_typing_section
        return file_import_copy.get_imports_from_section(baseline_typing_section)

    def _add_type_checking_import(self):
        any_typing = any(self.file_import.get_imports_from_section(TypingSection.TYPING))
        conditional_and_not_py3 = not self.is_python3_file and any(
            self.file_import.get_imports_from_section(TypingSection.CONDITIONAL)
        )
        if any_typing or conditional_and_not_py3:
            self.file_import.add_submodule_import("typing", "TYPE_CHECKING", ImportType.STDLIB)

    def _get_typing_definitions(self) -> str:
        def declare_defintion(spacing: int, type_name: str, type_definition: TypeDefinition) -> List[str]:
            ret: List[str] = []
            definition_value = type_definition.async_definition if self.async_mode else type_definition.sync_definition
            if type_definition.except_imports is None:
                ret.append("{}{} = {}".format(spacing, type_name, definition_value))
            else:
                ret.append("{}try:".format((spacing)))
                ret.append("    {}{} = {}".format(spacing, type_name, definition_value))
                ret.append("{}except {}:".format(spacing, type_definition.except_type))
                ret.extend(map(lambda x: "    {}{}  # pylint: disable=W0404".format(spacing, x),
                                _get_import_clauses(type_definition.except_imports, "\n    ")))
                ret.append("    {}{} = {}".format(spacing, type_name, definition_value))
            return ret

        if not self.file_import.type_definitions:
            return ""
        spacing = "" if self.is_python3_file else "    "
        declarations: List[str] = [""]
        for type_name, value in self.file_import.type_definitions.items():
            declarations.extend(declare_defintion(spacing, type_name, value))
        return "\n".join(declarations)

    def __str__(self) -> str:
        self._add_type_checking_import()
        regular_imports = ""
        regular_imports_list = self._get_imports_list(
            baseline_typing_section=TypingSection.REGULAR, add_conditional_typing=self.is_python3_file
        )

        if regular_imports_list:
            regular_imports = "\n\n".join(
                _get_import_clauses(regular_imports_list, "\n")
            )

        typing_imports = ""
        typing_imports_list = self._get_imports_list(
            baseline_typing_section=TypingSection.TYPING, add_conditional_typing=not self.is_python3_file
        )
        if typing_imports_list:
            typing_imports += "\n\nif TYPE_CHECKING:\n    # pylint: disable=unused-import,ungrouped-imports\n    "
            typing_imports += "\n\n    ".join(_get_import_clauses(typing_imports_list, "\n    "))
        return regular_imports + typing_imports + self._get_typing_definitions()
