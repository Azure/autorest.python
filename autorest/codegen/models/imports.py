# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum
from typing import Dict, Optional, List, Tuple, Callable, Set, Union


class ImportType(str, Enum):
    STDLIB = "stdlib"
    THIRDPARTY = "thirdparty"
    AZURECORE = "azurecore"
    LOCAL = "local"

class TypingSection(str, Enum):
    REGULAR = "regular"  # this import is always a typing import
    CONDITIONAL = "conditional"  # is a typing import when we're dealing with files that py2 will use, else regular
    TYPING = "typing"  # never a typing import

class SingularImport:
    def __init__(
        self,
        typing_section: TypingSection,
        import_type: ImportType,
        name: str,
        *,
        from_section: Optional[str] = None,
        alias: Optional[str] = None
    ):
        self.typing_section = typing_section
        self.import_type = import_type
        self.name = name
        self.from_section = from_section
        self.alias = alias

    def __eq__(self, other):
        try:
            return (
                self.typing_section == other.typing_section and
                self.import_type == other.import_type and
                self.name == other.name and
                self.from_section == other.from_section and
                self.alias == other.alias
            )
        except AttributeError:
            return False

    def __hash__(self):
        retval: int = 0
        for attr in dir(self):
            if attr[0] != "_":
                retval += hash(getattr(self, attr))
        return retval


class FileImport:
    def __init__(
        self,
        imports: List[SingularImport] = None
    ) -> None:
        self._imports = imports or []
        self._imports_dict: Dict[
            TypingSection,
            Dict[ImportType, Dict[str, Set[Optional[Union[str, Tuple[str, str]]]]]]
        ] = dict()
        # has sync and async type definitions
        self.type_definitions: Dict[str, Tuple[str, str]] = {}

    def to_dict(self) -> Dict[
            TypingSection,
            Dict[ImportType, Dict[str, Set[Optional[Union[str, Tuple[str, str]]]]]]
        ]:
        return self._imports_dict

    def get_from_predicate(self, predicate: Callable[[SingularImport], bool]) -> List[SingularImport]:
        return [i for i in self.imports if predicate(i)]

    @property
    def imports(self) -> List[SingularImport]:
        return list(set(self._imports))

    def _add_import(
        self,
        from_section: str,
        import_type: ImportType,
        typing_section: TypingSection = TypingSection.REGULAR,
        name_import: Optional[str] = None,
        alias: Optional[str] = None,

    ) -> None:
        last_entry: Optional[Union[str, Tuple[str, str]]] = None
        if not name_import:
            last_entry = None
        elif alias:
            last_entry = (name_import, alias)
        else:
            last_entry = name_import
        self._imports_dict.setdefault(
            typing_section, dict()
        ).setdefault(
            import_type, dict()
        ).setdefault(
            from_section, set()
        ).add(last_entry)
        self._imports.append(SingularImport(
            typing_section=typing_section,
            import_type=import_type,
            name=name_import if name_import else from_section,
            from_section=from_section if name_import else None,
            alias=alias,
        ))

    def add_from_import(
        self,
        from_section: str,
        name_import: str,
        import_type: ImportType,
        typing_section: TypingSection = TypingSection.REGULAR,
        alias: Optional[str] = None,
    ) -> None:
        """Add an import to this import block.
        """
        self._add_import(
            from_section, import_type, typing_section, name_import, alias
        )

    def add_import(
        self,
        name_import: str,
        import_type: ImportType,
        typing_section: TypingSection = TypingSection.REGULAR
    ) -> None:
        # Implementation detail: a regular import is just a "from" with no from
        self._add_import(name_import, import_type, typing_section)

    def define_mypy_type(self, type_name: str, type_value: str, async_type_value: Optional[str] = None):
        self.add_from_import("typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL)
        self.type_definitions[type_name] = (type_value, async_type_value or type_value)

    def merge(self, file_import: "FileImport") -> None:
        """Merge the given file import format."""
        self._imports.extend(file_import.imports)
        self.type_definitions.update(file_import.type_definitions)
