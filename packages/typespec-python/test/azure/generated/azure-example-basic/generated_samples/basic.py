# coding=utf-8
None

from specs.azure.example.basic import AzureExampleClient

"""
# PREREQUISITES
    pip install specs-azure-example-basic
# USAGE
    python basic.py
"""


def main():
    client = AzureExampleClient()

    response = client.basic_action(
        body={
            "arrayProperty": ["item"],
            "modelProperty": {"enumProperty": "EnumValue1", "float32Property": 1.5, "int32Property": 1},
            "recordProperty": {"record": "value"},
            "stringProperty": "text",
        },
        query_param="query",
        header_param="header",
    )
    print(response)


# x-ms-original-file: 2022-12-01-preview/basic.json
if __name__ == "__main__":
    main()
