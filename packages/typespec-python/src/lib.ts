import { SdkContext, SdkServiceOperation } from "@azure-tools/typespec-client-generator-core";
import { createTypeSpecLibrary, JSONSchemaType } from "@typespec/compiler";
import { PythonEmitterOptions, PythonEmitterOptionsSchema } from "@typespec/http-client-python";

export interface PythonAzureEmitterOptions extends PythonEmitterOptions {
    "generate-sample"?: boolean;
    "generate-test"?: boolean;
}

export interface PythonSdkContext<TServiceOperation extends SdkServiceOperation>
    extends SdkContext<PythonAzureEmitterOptions, TServiceOperation> {
    __endpointPathParameters: Record<string, any>[];
}

const PythonAzureEmitterOptionsSchema: JSONSchemaType<PythonAzureEmitterOptions> = {
    type: "object",
    additionalProperties: true,
    properties: {
        "generate-sample": {
            type: "boolean",
            nullable: true,
            description:
                "Whether to generate sample files, for basic samples of your generated sdks. Defaults to `false`.",
        },
        "generate-test": {
            type: "boolean",
            nullable: true,
            description:
                "Whether to generate test files, for basic testing of your generated sdks. Defaults to `false`.",
        },
        ...PythonEmitterOptionsSchema.properties,
    },
    required: [],
};

const libDef = {
    name: "@azure-tools/typespec-python",
    diagnostics: {},
    emitter: {
        options: PythonAzureEmitterOptionsSchema,
    },
} as const;

export const $lib = createTypeSpecLibrary(libDef);
export const { reportDiagnostic, createStateSymbol, getTracer } = $lib;
