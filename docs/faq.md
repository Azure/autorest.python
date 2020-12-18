# <img align="center" src="./images/logo.png">  FAQ

1. What are the minimum dependencies?

    The minimum dependencies are listed [here][min_dependencies]. This list will be continuously updated.

2. What version of AutoRest Python should I use?

    We highly recommend you use the latest AutoRest Python version published to [npm][autorest_npm]. The latest version
    is the default if you use flag `--python`, though you may need to run an `autorest --reset` if it seems
    the latest version is not being grabbed.

    If you *really* want to use an older version of AutoRest Python,
    you can specify the version with the flag `--use`, i.e. `--use=@autorest/python@5.x.x`.


<!-- LINKS -->
[min_dependencies]: ./client/initializing.md#minimum-dependencies-of-your-client
[autorest_npm]: https://www.npmjs.com/package/@autorest/python