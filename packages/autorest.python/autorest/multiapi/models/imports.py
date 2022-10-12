# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum
from typing import Dict, Optional, Set, Union, Tuple


class ImportType(str, Enum):
    STDLIB = "stdlib"
    THIRDPARTY = "thirdparty"
    AZURECORE = "azurecore"
    LOCAL = "local"


class TypingSection(str, Enum):
    REGULAR = "regular"  # this import is always a typing import
    CONDITIONAL = "conditional"  # is a typing import when we're dealing with files that py2 will use, else regular
    TYPING = "typing"  # never a typing import


class FileImport:
    def __init__(
        self,
        imports: Dict[
            TypingSection,
            Dict[
                ImportType,
                Dict[
                    str,
                    Set[
                        Optional[
                            Union[
                                str,
                                Tuple[
                                    str,
                                    str,
                                ],
                                Tuple[
                                    str,
                                    str,
                                    Tuple[Tuple[Tuple[int, int], str, Optional[str]]],
                                ],
                            ]
                        ]
                    ],
                ],
            ],
        ] = None,
    ) -> None:
        # Basic implementation
        # First level dict: TypingSection
        # Second level dict: ImportType
        # Third level dict: the package name.
        # Fourth level set: None if this import is a "import", the name to import if it's a "from"
        self._imports: Dict[
            TypingSection,
            Dict[
                ImportType,
                Dict[
                    str,
                    Set[
                        Optional[
                            Union[
                                str,
                                Tuple[
                                    str,
                                    str,
                                ],
                                Tuple[
                                    str,
                                    str,
                                    Tuple[Tuple[Tuple[int, int], str, Optional[str]]],
                                ],
                            ]
                        ]
                    ],
                ],
            ],
        ] = (
            imports or dict()
        )

    @staticmethod
    def _convert_list_to_tuple(l):
        return (
            tuple(FileImport._convert_list_to_tuple(x) for x in l)
            if isinstance(l, list)
            else l
        )

    def _add_import(
        self,
        from_section: str,
        import_type: ImportType,
        name_import: Optional[
            Union[
                str,
                Tuple[
                    str,
                    str,
                ],
                Tuple[str, str, Tuple[Tuple[Tuple[int, int], str, Optional[str]]]],
            ]
        ] = None,
        typing_section: TypingSection = TypingSection.REGULAR,
    ) -> None:
        name_input: Optional[
            Union[
                str,
                Tuple[
                    str,
                    str,
                ],
                Tuple[str, str, Tuple[Tuple[Tuple[int, int], str, Optional[str]]]],
            ]
        ] = None
        if isinstance(name_import, list):
            name_input = self._convert_list_to_tuple(name_import)
        else:
            name_input = name_import
        self._imports.setdefault(typing_section, dict()).setdefault(
            import_type, dict()
        ).setdefault(from_section, set()).add(name_input)

    def add_submodule_import(
        self,
        from_section: str,
        name_import: str,
        import_type: ImportType,
        typing_section: TypingSection = TypingSection.REGULAR,
    ) -> None:
        """Add an import to this import block."""
        self._add_import(from_section, import_type, name_import, typing_section)

    @property
    def imports(
        self,
    ) -> Dict[
        TypingSection,
        Dict[
            ImportType,
            Dict[
                str,
                Set[
                    Optional[
                        Union[
                            str,
                            Tuple[
                                str,
                                str,
                            ],
                            Tuple[
                                str,
                                str,
                                Tuple[Tuple[Tuple[int, int], str, Optional[str]]],
                            ],
                        ]
                    ]
                ],
            ],
        ],
    ]:
        return self._imports

    def merge(self, file_import: "FileImport") -> None:
        """Merge the given file import format."""
        for typing_section, import_type_dict in file_import.imports.items():
            for import_type, package_list in import_type_dict.items():
                for package_name, module_list in package_list.items():
                    for module_name in module_list:
                        self._add_import(
                            package_name, import_type, module_name, typing_section
                        )
