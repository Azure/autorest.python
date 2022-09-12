# Python CADL Archboard Presentation

## DPG Parity

In this first section we're going to be talking about parity with current DPG generations from swagger. As a reminder, Python does not generate any models currently with our DPG generations, we only deal with JSON. In this first section, Yuchao will go over what our generated CADL looks like without models, showing complete parity with what we currently generate with DPG. I will then introduce our new models we're exclusively offering for Cadl generations, then Changlong will show you how we are going to grow up our current operations to handle our new models.

Thanks Isabella. Hello, everyone. This is Yuchao. Please allow me to show you DPG parity of Python with three samples: Get/Post/Paging. First one is Get.

### GET

Here is a Cadl describing a `get` on a project class. It is very simple, so let us see the **signature and usage**.

```cadl
@doc("Gets the details of a project.")
get is ResourceRead<Project>;
```

#### Signature

From the **signature**, we can see: without models, we still return a raw JSON object. 


```python
def get(
  self,
  project_name: str,
  *,
  **kwargs: Any
) -> JSON:
```

#### Usage

From the **usage**, we can see: users can access the response object like a dictionary with square brackets, and all of the information is in its serialized form. 

```python
project = client.projects.get("my-project")

assert project["projectName"] == "my-project"
assert project["createdDateTime"] == "2022-09-12T00:00:00Z"
```

Is it consistent with SDKs from swagger? The answer is Yes. Absolutely! Ok, let us see next sample: Post.

### POST

The cadl shows that we are looking at accepting a body as input and passing it to the service. Actually, this function is not in the QnA authoring cadl, but I think it's more to demonstrate what an input body would look like. Let us see its signature.

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

The **usage** shows users can pass in the body as JSON object. And I also want to emphasize that it is exactly same with SDK from swagger. Ok, let's see next sample: Paging.

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

Here's cadl definion: It is paging operation with query parameters. And the generated signature is here:

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

For paging, like we do for DPG, we can still return an iterable of JSON objects. And users can access final result with pyhonic loop which is showed in **usge** part.

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

For the same question? Of course yes.

```python
projects = client.projects.list()
for project in projects:
  print(project["projectName"])
  print(project["createdDateTime"])
```

Ok, with the 3 samples, we have shown the DPG parity in python for most common scenarios. However, there are some known cadl issues for parity.

### Known Cadl Issues for Parity (Yuchao)

- 1) LRO: (merged but not stable released. But I think there will be stable release soon)
- 2) Multiple input body types: https://github.com/microsoft/cadl/issues/756
- 3) Skip URL encoding: It is issue about the Way to skip or specify to urlencode a parameter
- 4) Sidecar support: Add support for sidecar client definition for complex clients
- 5) Client and subclient


That's all of my part. Thanks!
