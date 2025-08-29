# Setting up

The tutorial will take you through using `pyproject.toml` in an example
codebase. Before you start, you need to set up your environment.

These setup steps assume that you have access to:

- a Python installation (version 3.8 or more recent),
- a way to run Python from a shell,
- an internet connection.

## Create an environment

The tutorial will have you install various packages. To avoid interfering
with other Python projects you may have, use a virtual environment.
This can be done with the [`venv` package][venv-guide]
from the Python standard library.

!!! note
    - The commands below assume Python 3.12. Substitute your own version when
    calling the `python` executable.
    - If you are using Anaconda, you can create and activate the environment
    using the `conda` commands instead of the below.


1. In a shell, create a virtual environment by running the command:

    === "Linux/Mac/WSL"
        ```console
        python3.12 -m venv pyproject-tutorial
        ```

    === "Windows"
        ```console
        py -m venv pyproject-tutorial
        ```

1. Activate the environment with

    === "Linux/Mac/WSL"

        ```console
        source pyproject-tutorial/bin/activate
        ```

    === "Windows"
        ```console
        pyproject-tutorial\Scripts\activate
        ```

You will be installing Python packages into this virtual environment
through the course of the tutorial. While you keep this shell open,
the environment will remain active unless you deactivate it.

## Get the starter code

Download the starter code by going to the [Releases page][release],
downloading the `pyproject-sample.zip` file and unzipping it.

You should have the following structure:

```
(project root)
├── pyproject.toml
└── src
    ├── LICENSE
    └── my_package
        ├── __init__.py
        ├── cli.py
        ├── experimental.py
        └── library.py
```

The `pyproject.toml` contains a very basic configuration, which you will
be extending during the tutorial.
The rest of the code is only there as an example and does not do anything
particularly interesting!
It has also purposefully been written to contain some issues, which you
will be fixing with the tools covered in the tutorial.


You're now ready to start!

[venv-guide]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments
[release]: https://github.com/ageorgou/pyproject-toml/releases/latest