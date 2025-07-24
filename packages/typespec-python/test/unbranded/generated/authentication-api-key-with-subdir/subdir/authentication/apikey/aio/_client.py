from .._generated.aio import ApiKeyClient

class CustomizedApiKeyClient(ApiKeyClient):
    """Customized ApiKeyClient with additional functionality."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initialization or customization can be done here

    def custom_method(self):
        """An example of a custom method that extends the functionality."""
        print("This is a custom method in the CustomizedApiKeyClient.")
