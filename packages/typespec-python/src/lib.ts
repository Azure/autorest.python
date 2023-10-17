import { createTypeSpecLibrary, JSONSchemaType } from "@typespec/compiler";

export interface PythonEmitterOptions {
    "package-version"?: string;
    "package-name"?: string;
    "output-dir"?: string;
    "generate-packaging-files"?: boolean;
    "package-pprint-name"?: string;
    "head-as-boolean"?: boolean;
    "models-mode"?: string;
    "unbranded"?: boolean;
    "tracing"?: boolean;
    "debug"?: boolean;
}

const EmitterOptionsSchema: JSONSchemaType<PythonEmitterOptions> = {
    type: "object",
    additionalProperties: true,
    properties: {
        "package-version": { type: "string", nullable: true },
        "package-name": { type: "string", nullable: true },
        "output-dir": { type: "string", nullable: true },
        "generate-packaging-files": { type: "boolean", nullable: true },
        "package-pprint-name": { type: "string", nullable: true },
        "head-as-boolean": { type: "boolean", nullable: true },
        "models-mode": { type: "string", nullable: true },
        "unbranded": { type: "boolean", nullable: true },
        "tracing": { type: "boolean", nullable: true },
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
