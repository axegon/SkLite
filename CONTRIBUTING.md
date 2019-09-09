# Contributing to sklite

As an open source projects, contributions are welcome.

## Issues

When you encounter an issue with any of the modules in this package please open a new issue and include the following information:

* Python version.
* OS.
* Dataset or partial dataset with which the issue can be reproduced.
* Expected result.
* Result you got.

## Documentation

Contributing to the documentation is highly appreciated. Simply fork the repository, make the changes in your own fork under the `docs/` directory, build the documentation, push it to your fork and create a PR including a short description of the changes you've made.

## Contributing to the code

Same as the documentation, naturally. if you are making changes to any of the existing models, start by creating new tests which cover the current implementations, as well as the changes you want to add. Once you have those, make the changes you wish to make and run them against the tests. If all tests pass, commit the changes to your fork and open a PR with a description of your changes. Add documentation wherever possible.

## Coding style

The repository uses PEP8 coding style, with numpy docstrings. before opening a PR, make sure you have ran the shell scripts under `build_scripts/` and they all pass.

