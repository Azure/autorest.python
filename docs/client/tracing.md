# <img align="center" src="../images/logo.png">  Tracing

Our generated code natively supports tracing with [`OpenTelemetry`][open_telemetry]. To do so, generate with flag `--trace` (see our [flag index][flag_index] for more information).

> **Note:** [`OpenCensus`][open_census] has been deprecated and is no longer supported. Please use [`OpenTelemetry`][open_telemetry] for tracing.

## OpenTelemetry

First step is to install our [`OpenTelemetry` library][our_open_telemetry_library]:

```python
pip install azure-core-tracing-opentelemetry
```

Our generated SDKs handle retrieving context for you, so there's no need to pass in any context.
Since there is no explicit context you need to pass, you can create your usual OpenTelemetry tracer and call the generated SDKs.
The following example uses a console exporter, but you can use any exporter ([`Azure Monitor`][azure_monitor], [Zipkin][zipkin], etc.).

```python
from azure.core.settings import settings
from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan

settings.tracing_implementation = OpenTelemetrySpan

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

exporter = ConsoleSpanExporter()

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(exporter)
)

from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
dog = client.get_dog()  # Call will be traced
```

<!-- LINKS -->
[open_census]: https://opencensus.io/
[open_telemetry]: https://opentelemetry.io/
[flag_index]: https://github.com/Azure/autorest/tree/master/docs/generate/flags.md
[azure_monitor]: https://pypi.org/project/opentelemetry-azure-monitor/
[zipkin]: https://zipkin.io/
[our_open_telemetry_library]: https://pypi.org/project/azure-core-tracing-opentelemetry/
