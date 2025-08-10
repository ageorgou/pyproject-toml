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
   ```console
   python3 -m venv pyproject-tutorial
   ```
1. Activate the environment with
    ```console
    source pyproject-tutorial/bin/activate
    ```


## Get the starter code

- Copy the starting code

[venv-guide]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments