# Python CADL Archboard Presentation

## DPG Parity

In this first section we're going to be talking about parity with current DPG generations from swagger. As a reminder, Python does not generate any models currently with our DPG generations, we only deal with JSON. In this first section, Yuchao will go over what our generated CADL looks like without models, showing complete parity with what we currently generate with DPG. I will then introduce our new models we're exclusively offering for Cadl generations, then Changlong will show you how we are going to grow up our current operations to handle our new models.

### GET

Here is a Cadl documentation describing a simple get on a project class.

```cadl
@doc("Gets the details of a project.")
get is ResourceRead<Project>;
```

#### Signature

Without models, we still return a raw JSON object. Users access the response object like a dictionary with square brackets, and all of the information is in its serialized form. This is consistent with what we're doing with our DPG SDKs from swagger.

```python
def get(
  self,
  project_name: str,
  *,
  **kwargs: Any
) -> JSON:
```

#### Usage

```python
project = client.projects.get("my-project")

assert project["projectName"] == "my-project"
assert project["createdDateTime"] == "2022-09-12T00:00:00Z"
```

### POST

Here we are looking at accepting a body as input and passing it to the service. This function is not actually in the authoring cadl, but is more to demonstrate what an input body would look like

```cadl
@doc("Create a project.")
create is ResourceCreateOrUpdate<
  Project
>;
```

#### Signature

Like we do for DPG, we generate typing overloads so users can either pass in the body as a JSON object, or they can also stream a JSON file to the server if they don't want to load the body into memory.

```python
@overload
def create(
    self,
    project_name: str,
    body: JSON,
    *,
    content_type: str = "application/merge-patch+json",
    **kwargs: Any
) -> JSON:
    ...

@overload
def create(
    self,
    project_name: str,
    body: IO,
    *,
    content_type: str = "application/merge-patch+json",
    **kwargs: Any
) -> JSON:
    ...
```

#### Usage

```python
client.projects.create(
  "my-project",
  {
    "language": "en",
    "projectKind": "CustomEntityRecognition",
  },
)
```

### Paging

For paging, like we do for DPG, we can still return an iterable of JSON objects.

```cadl
model ListQueryParams {
  @query top?: int32;
  @query skip?: int32;
  @query maxpagesize?: int32;
}

@doc("Lists the existing projects.")
list is ResourceList<
  Project,
  {
    parameters: ListQueryParams;
  }
>;
```

#### Signature

```python
def list(
  self,
  project_name: str,
  *,
  top: Optional[int] = None,
  skip: Optional[int] = None,
  **kwargs: Any
) -> Iterable[JSON]:
```

#### Usage

```python
projects = client.projects.list()
for project in projects:
  print(project["projectName"])
  print(project["createdDateTime"])
```

### Known Cadl Issues for Parity (Yuchao)

- LRO:
- Multiple input body types: https://github.com/microsoft/cadl/issues/756
- Skip URL encoding: Way to skip or specify to urlencode a parameter
- Sidecar support: Add support for sidecar client definition for complex clients
- Client and subclient

## Added Feature: Models

### New Models (Isabella)

When Python first started thinking about the DPG story, we realized we wanted to update our entire model structure. To begin with, Python users are extremely comfortable with JSON (and in some cases even prefer JSON syntax to structured model syntax). In fact, this is feedback we'd been getting from our Python SDK users for a while, and that's why we still feel so comfortable just exposing JSON and providing template documentation to guide users. That being said, models still have their use cases: they are extremely helpful landing pages for documentation and intellisense, and they can also provide deserialization capabilities. Therefore we decided we wanted the best of both worlds and designed a model class that behaves both like a JSON dictionary and as a typed model.

#### Behaves like a JSON dict AND a model at the same time

Changlong will go more into how we're going to grow-up our existing methods to accept and return models, but basically since these models behave exactly like dicts as well, we can have the same function handle models instead of just pure JSON and be non-breaking.

Following our QnA Cadl, here is our generation for a `Project` class. For the purposes of the presentation, I'm only showing a couple of the properites of the Project class.

##### Output

```cadl
model Project {
  projectName: string;

  language: string;

  @visibility("read")
  createdDateTime: zonedDateTime;
}
```

```python
class Project:
  project_name: str = rest_field(name="projectName")
  language: str = rest_field()
  created_date_time: datetime.datetime = rest_field(name="createdDateTime", readonly=True)
```

```python
project = client.projects.get()
assert project["projectName"] == project.project_name == "my-project"
assert project["createdDateTime"] == "2022-09-12T00:00:00Z"
assert project.created_date_time == datetime(2022, 9, 12)
```

##### Input

You can create these models by passing in each of the properties by name, but you can also pass them in through a dictionary. For the first you get all of the intellisense and documentation benefits of a model when creating the model, for the latter, you can directly pass in a returned JSON object / model.

```python
project = Project(
    project_name="my-project",
    language="en",
)

######### OR #########

project = Project({
    "projectName": "my-project",
    "language": "en",
})
```

#### Deserialization

With this dual-form of model, we're able to accomodate both serialized and deserialized versions of properties. The JSON representation of the model will always represent the serialized version of the model, while the attribute representation will have additional deserialization capabilities

```python
assert project["createdDateTime"] == "2022-09-12T00:00:00Z"
assert project.created_date_time == datetime(2022, 9, 12)
```

#### Documentation and Intellisense

Models also provide better documentation and intellisense support. While our old templates are still good at depicting the necessary information, the models do offer a better overall documentation and intellisense experience.

##### Existing Template

<img width="652" alt="Screen Shot 2022-09-07 at 5 04 50 PM" src="https://user-images.githubusercontent.com/43154838/189005730-8e273e0e-723e-4d4a-97ea-ed541dc10a0f.png">

##### New Sphinx Documentation

<img width="741" alt="Screen Shot 2022-09-07 at 5 01 01 PM" src="https://user-images.githubusercontent.com/43154838/189005808-950e04d7-ae1b-4dac-814b-6e410c4326a5.png">

##### Intellisense

![Screen Shot 2022-09-07 at 3 40 27 PM](https://user-images.githubusercontent.com/43154838/189005829-9ede8e58-cc64-4b08-98c2-f3729804ba10.png)


#### Open Design Questions

- Defaults (talk about this)
- Potential polymorphism changes
- Constants
- Making readonly properties not settable

### Integration of Models into Methods (Changlong)

#### Get

For response models, we can directly grow up the same function to just return our new model instead of a raw JSON object. This is because when accessed like a dictionary, our new models behave exactly the same as a raw JSON object.

##### Signature

<table>
<tr>
<td> Before </td> <td> After </td>
</tr>
<tr>
<td>

```python
def get(
  self,
  project_name: str,
  *,
  **kwargs: Any
) -> JSON:
```

</td>
<td>

```python
def get(
  self,
  project_name: str,
  *,
  **kwargs: Any
) -> Project:
```

</td>
</tr>
</table>

##### Usage

```python
project = client.projects.get("my-project")

assert project["projectName"] == "my-project"
assert project["createdDateTime"] == "2022-09-12T00:00:00Z"

######### AND #########
assert project.created_date_time == datetime(2022, 9, 12)
```

#### Post

For input models, we accept both raw JSON and our new models as input. Users can still pass in their raw JSON dictionaries to our methods, or they can create / pass in the output from another function. This way users get better documentation landing pages, and if they decide they want to create their own model, they get an improved intellisense experience as well.

##### Signature

<table>
<tr>
<td> Before </td> <td> After </td>
</tr>
<tr>
<td>

```python
@overload
def create(
    self,
    project_name: str,
    body: JSON,
    *,
    content_type: str = "application/merge-patch+json",
    **kwargs: Any
) -> JSON:
    ...

@overload
def create(
    self,
    project_name: str,
    body: IO,
    *,
    content_type: str = "application/merge-patch+json",
    **kwargs: Any
) -> JSON:
    ...
```

</td>
<td>

```python
@overload
def create(
    self,
    project_name: str,
    body: Project,
    *,
    content_type: str = "application/merge-patch+json",
    **kwargs: Any
) -> Project:
    ...

@overload
def create(
    self,
    project_name: str,
    body: IO,
    *,
    content_type: str = "application/merge-patch+json",
    **kwargs: Any
) -> Project:
    ...
```

</td>
</tr>
</table>

##### Usage

```python
client.projects.create(
  "my-project",
  {
    "language": "en",
    "projectKind": "CustomEntityRecognition",
  },
)

######### AND #########

from azure.language.authoring.models import Project
client.projects.train(
    "my-project",
    Project(
        language="en",
        project_kind="CustomEntityRecognition",
    ),
)
```

#### Paging

We also support paging iteration of models, so just like our previous get call, users have the flexibility to treat the response as either an iterable of dicts or an iterable of models.

##### Signature

<table>
<tr>
<td> Before </td> <td> After </td>
</tr>
<tr>
<td>

```python
def list(
    self,
    *,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    **kwargs: Any
) -> Iterable[JSON]
```

</td>
<td>

```python
def list(
    self,
    *,
    top: Optional[int] = None,
    skip: Optional[int] = None,
    **kwargs: Any
) -> Iterable[Project]
```

</td>
</tr>
</table>

##### Usage

```python
projects = client.projects.list()
for project in projects:
  print(project["projectName"])  # my-project
  print(project["createdDateTime"])  # 2022-09-12T00:00:00Z

  ######### AND #########

  print(project.project_name)  # my-project
  print(project.created_date_time)  # datetime(2022, 9, 12)
```
