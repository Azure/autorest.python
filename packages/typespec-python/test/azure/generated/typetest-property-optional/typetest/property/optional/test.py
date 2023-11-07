from typetest.property.optional.models import Test, TestProperties



test = Test(name="old")
assert test.properties.name == "old"
