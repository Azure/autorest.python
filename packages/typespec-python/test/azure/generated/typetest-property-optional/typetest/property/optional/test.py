from typetest.property.optional.models import Test, TestProperties

# test = Test(properties=TestProperties(name="old"))
# assert test.name == "old"
# test = Test({"properties": {"name": "old"}})
# assert test.name == "old"

# test = Test()
# assert test.properties is None
# assert test.name is None

test = Test(name="old")
assert test.properties.name == "old"
assert test.name == "old"

# test.name = "new"
# assert test.properties.name == "new"
# test.properties.name = "newer"
# assert test.name == "newer"
