import json
from authentication.apikey.models import InvalidAuth
from authentication.apikey._utils.model_base import SdkJSONEncoder, _deserialize
from azure.core.messaging import CloudEvent

cloud_event = CloudEvent(source="source", type="type")

# serialize
print("========= serialize =================")
model = InvalidAuth(error="error", cloud_event=cloud_event)
print(model.cloud_event.source)
print(model.cloud_event.type)
print(json.dumps(model, cls=SdkJSONEncoder))

# deserialize (external type as model property) 
print("========= deserialize (external type as model property) =================")
model_from_dict = _deserialize(InvalidAuth, {"error": "error", "cloudEvent": {"source": "source", "type": "type"}})
print(model_from_dict.cloud_event.source)
print(model_from_dict.cloud_event.type)

# deserialize external type directly
print("========= deserialize external type directly =================")
cloud_event_from_dict = _deserialize(CloudEvent, {"source": "source", "type": "type"})
print(cloud_event_from_dict.source)
print(cloud_event_from_dict.type)
