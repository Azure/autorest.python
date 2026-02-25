# Developing and Contributing

## Testing `@azure-tools/typespec-python` Tarballs

To test an unpublished branded emitter tarball, please follow these steps:

1. Go to the pipelines and find the run you'd like to test [here](https://dev.azure.com/azure-sdk/public/_build?definitionId=1316&_a=summary)
2. Open the run and find the artifacts published as part of that run.
3. Choose the published artifact you'd like to test, there will be one for each matrix run.
4. Click on the three dots and click "Copy download url"
5. Copy-paste that url, then head over to the [`emitter-package.json`](https://github.com/Azure/azure-sdk-for-python/blob/main/eng/emitter-package.json) in the [`azure-sdk-for-python`](https://github.com/Azure/azure-sdk-for-python/tree/main) repo
6. Paste the url as the version for the `"@azure-tools/typespec-python"` package
7. Run `tsp-client generate-lock-file` from the `azure-sdk-for-python/eng` folder
8. Go to the sdk you'd like to regenerate with the tarball, then run `tsp-client update` how you normally would

## Design Notes

- [`Http.File` request body compatibility for Python](./http_file_body_compatibility.md)
