# <img align="center" src="../images/logo.png">  Tracing

Our generated code can natively support tracing libraries [`OpenCensus`][open_census] and [`OpenTelemetry`][open_telemetry]. To do so, generate with flag `--trace` (see our [flag index][flag_index] for more information).

## OpenCensus

First step is to install our [`OpenCensus` library][our_open_census_library]:

```python
pip install azure-core-tracing-opencensus
```

Our generated SDKs handle retrieving context for you, so there's no need to pass in any context. Additionally, the
OpenCensus threading plugin is included when installing this package.

Since there is no explicit context you need to pass, you can create your usual OpenCensus tracer and call the generated SDKs.
The following example uses [`Azure Monitor`'s][azure_monitor] exporter, but you can use any exporter ([Zipkin][zipkin], etc.).

```python
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.tracer import Tracer
from opencensus.trace.samplers import AlwaysOnSampler

from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

exporter = AzureExporter(
    instrumentation_key="uuid of the instrumentation key (see your Azure Monitor account)"
)
tracer = Tracer(exporter=exporter, sampler=AlwaysOnSampler())
with tracer.span(name="MyApplication") as span:
    client = PetsClient(credential=DefaultAzureCredential())
    dog = client.get_dog()  # Call will be traced
```

## OpenTelemetry

First step is to install our [`OpenTelemetry` library][our_open_telemetry_library]:

```python
pip install azure-core-tracing-opentelemetry
```

Our generated SDKs handle retrieving context for you, so there's no need to pass in any context.
Since there is no explicit context you need to pass, you can create your usual OpenTelemetry tracer and call the generated SDKs.
The following example uses [`Azure Monitor`'s][azure_monitor] exporter, but you can use any exporter ([Zipkin][zipkin], etc.).

```python
# Declare OpenTelemetry as an enabled tracing plugin for Azure SDKs
from azure.core.settings import settings
from azure.core.tracing.ext.opentelemetry_span import OpenTelemetrySpan

settings.tracing_implementation = OpenTelemetrySpan

# In the below example, we use the Azure Monitor exporter, but you can use anything OpenTelemetry supports
from azure_monitor import AzureMonitorSpanExporter
exporter = AzureMonitorSpanExporter(
    instrumentation_key="uuid of the instrumentation key (see your Azure Monitor account)"
)

# Regular open telemetry usage from here, see https://github.com/open-telemetry/opentelemetry-python
# for details
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor

# Simple console exporter
exporter = ConsoleSpanExporter()

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(exporter)
)

# Example with our Pets example
from azure.identity import DefaultAzureCredential
from azure.pets import PetsClient

client = PetsClient(credential=DefaultAzureCredential())
dog = client.get_dog()  # Call will be traced
```

<!-- LINKS -->
[open_census]: https://opencensus.io/
[open_telemetry]: https://opentelemetry.io/
[flag_index]: https://github.com/Azure/autorest/tree/master/docs/generate/flags.md
[our_open_census_library]: https://pypi.org/project/azure-core-tracing-opencensus/
[azure_monitor]: https://pypi.org/project/opentelemetry-azure-monitor/
[zipkin]: https://zipkin.io/
[our_open_telemetry_library]: https://pypi.org/project/azure-core-tracing-opentelemetry/
