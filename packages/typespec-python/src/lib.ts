import { createTypeSpecLibrary, JSONSchemaType } from "@typespec/compiler";

export interface PythonEmitterOptions {
    "basic-setup-py"?: boolean;
    "package-version"?: string;
    "package-name"?: string;
    "output-dir"?: string;
    "package-mode"?: string;
    "package-pprint-name"?: string;
    "head-as-boolean"?: boolean;
    "models-mode"?: string;
    "debug"?: boolean;
}

const EmitterOptionsSchema: JSONSchemaType<PythonEmitterOptions> = {
    type: "object",
    additionalProperties: true,
    properties: {
        "basic-setup-py": { type: "boolean", nullable: true },
        "package-version": { type: "string", nullable: true },
        "package-name": { type: "string", nullable: true },
        "output-dir": { type: "string", nullable: true },
        "package-mode": { type: "string", nullable: true },
        "package-pprint-name": { type: "string", nullable: true },
        "head-as-boolean": { type: "boolean", nullable: true },
        "models-mode": { type: "string", nullable: true },
        "debug": { type: "boolean", nullable: true },
    },
    required: [],
};

const libDef = {
    name: "@azure-tools/typespec-python",
    diagnostics: {},
    emitter: {
        options: EmitterOptionsSchema as JSONSchemaType<PythonEmitterOptions>,
    },
} as const;

export const $lib = createTypeSpecLibrary(libDef);
export const { reportDiagnostic, createStateSymbol, getTracer } = $lib;
