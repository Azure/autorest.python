import { EmitContext } from "@typespec/compiler";
import { PythonEmitterOptions } from "./lib.js";
import { $onEmit as httpClientPythonOnEmit } from "../node_modules/@typespec/http-client-python/emitter/src/emitter.js";

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
    return httpClientPythonOnEmit(context);
}
