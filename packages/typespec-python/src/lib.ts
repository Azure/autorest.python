import { SdkContext, SdkServiceOperation, BrandedSdkEmitterOptions } from "@azure-tools/typespec-client-generator-core";
import { createTypeSpecLibrary, JSONSchemaType } from "@typespec/compiler";
import { PythonEmitterOptions, PythonEmitterOptionsSchema } from "@typespec/http-client-python";

export interface PythonAzureEmitterOptions extends PythonEmitterOptions {
    "examples-dir"?: string;
    "namespace"?: string;

    "flavor"?: "azure";
    "models-mode"?: string;
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
        ...BrandedSdkEmitterOptions["examples-dir"],
        ...BrandedSdkEmitterOptions["namespace"],

        "flavor": {
            type: "string",
            nullable: true,
            description: "The flavor of the SDK.",
        },
        "models-mode": {
            type: "string",
            nullable: true,
            enum: ["dpg", "none"],
            description:
                "What kind of models to generate. If you pass in `none`, we won't generate models. `dpg` models are the default models we generate.",
        },
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
