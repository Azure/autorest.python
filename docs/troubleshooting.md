# <img align="center" src="./images/logo.png">  Troubleshooting

## Generation Errors

There are two broad kinds of errors you can run into when generating: one kind is thrown earlier in the AutoRest pipeline and has to do with malformed swaggers (see [our main docs][main_docs] for more information). The other kind is thrown by the Python generator itself.

The general AutoRest errors are thrown like this

```
FATAL: Error: Enum types of 'object' and format 'undefined' are not supported. Correct your input (HdiNodeTypes).
  Error: Plugin modelerfour reported failure.
```

While the Python generator throws Python errors, such as:

```
ERROR: [main.Process:52] Python generator raised an exception
Traceback (most recent call last):
  ...
ValueError: --credential-scopes must be used with the --add-credential flag
  Error: Plugin codegen reported failure.
```

Both of these issues should give you enough information to fix the error. If not, please let us know in either the [main repo][autorest_issues], or in the [Python repo][autorest_python_issues]. Also let us know if you believe
there are erroneous errors being thrown.

## Debugging

Our [main docs][main_debugging] show you how to pass in flags (`--verbose` / `--debug`) to get more debugging logs for your AutoRest calls.

If you'd like to actually debug through our code, you need to first clone our [repo]. These debugging steps are specific to VS Code.

Once debugging our code, you need to add this to the VSCode launch configuration (`launch.json`). This configuration tells VS Code to attach at port `5678`, the default port.

```
{
    "name": "Python: Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost"
}
```

Once this has been successfully added, all that's needed is to add flag `--python.debugger` on our command line. You should now be able to step through the Python generator's code base.

<!-- LINKS -->
[main_docs]: https://github.com/Azure/autorest/tree/master/docs/troubleshooting.md
[autorest_issues]: https://github.com/Azure/autorest/issues
[autorest_python_issues]: https://github.com/Azure/autorest.python/issues
[main_debugging]: https://github.com/Azure/autorest/tree/master/docs/troubleshooting.md#debugging
[autorest_python_repo]: https://github.com/Azure/autorest.python/tree/autorestv3