# Packaging

A main use of `pyproject.toml` is for defining project metadata.
This includes:

- the name of your project, and your contact information,
- the versions of Python it is compatible with,
- the packages it depends on,
- the command-line tools it provides.

This information is used to build and install the project,
as well as when publishing it on PyPI.

All this information is stored in the `[project]` table of the
`pyproject.toml` file.

## Basic metadata
Add the following section to your file:

```toml
[project]
name = "my-package"
version = "1.0"
authors =  [
    {name = "Firstname Lastname", email = "me@me.org"}
]
description = "A really cool project"
license = "Apache-2.0"
license-files = ["LICENSE.md"]
keywords = ["science", "magic"]
```

You can change the authors or project name to values of your choice.

Note that:

- The project `name` is how other projects will refer to yours,
e.g. when declaring their dependency on it.
- The `name` cannot contain spaces.
- The `keywords` make it easier to find your project on PyPI when searching
for those terms. 

!!! tip "Avoid hardcoding the version"

    You can set the version dynamically, based on some property in your code.

    Change the `version = "1.0"` line above to `dynamic = ["version"]`.
    Then add a new section:
    ```toml
    [tool.setuptools.dynamic]
    version = {attr = "my_package.__version__"}
    ```

    This will read the version from the `__version__` variable in
    `my_package/__init__.py`.

## Dependencies

## Entrypoints

## Further resources
- The Python Packaging Authority (PyPA) provides a comprehensive
[guide to writing a pyproject.toml file][pypa-guide].
- PyPA also maintains the latest version of the
[formal specification][pypa-spec].
- The docs for `setuptools` (the default build backend) include a
[guide][setuptools-toml] for how to configure `pyproject.toml` for it.
Other backends may have their own guidance.
- [PEP 621][pep-621] proposed what project metadata should be stored.

[pep-621]: https://peps.python.org/pep-0621
[pypa-spec]: https://packaging.python.org/en/latest/specifications/pyproject-toml/#pyproject-toml-spec
[pypa-guide]: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
[setuptools-toml]: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
