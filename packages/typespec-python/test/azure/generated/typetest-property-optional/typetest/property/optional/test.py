from typetest.property.optional.models import Test, TestProperties


test = Test(properties=TestProperties(name="old"))
assert test.name == "old"
test = Test({"properties": {"name": "old"}})
assert test.name == "old"

test = Test(name="old")
assert test.properties.name == "old"
test.name = "new"
assert test.properties.name == "new"
test.properties.name = "newer"
assert test.name == "newer"
