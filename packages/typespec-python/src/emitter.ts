import { EmitContext } from "@typespec/compiler";
import { PythonEmitterOptions } from "./lib.js";
import { $onEmit as httpClientPythonOnEmit } from "@typespec/http-client-python";

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
    return httpClientPythonOnEmit(context);
}
