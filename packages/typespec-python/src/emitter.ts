import { EmitContext } from "@typespec/compiler";
import { PythonEmitterOptions } from "./lib.js";
import { $onEmit as httpClientPythonOnEmit } from "@typespec/http-client-python";

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
    // set flavor to azure if not set for python azure emitter
    if (context.options.flavor === undefined) {
        context.options.flavor = "azure";
    }
    await httpClientPythonOnEmit(context);
}
