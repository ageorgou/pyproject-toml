# Linting

As codebases become larger, it is easier for mistakes to creep in.
**Linters** are tools that check the code for signs of potential problems,
like unused variables or uncommon usage patterns.

There are numerous linters for Python, and many of them can be configured
through `pyproject.toml`.
For this tutorial, we will use `ruff`, a relatively recent suite of linting
and formatting tools.


## Install the linter
The linter is an optional dependency: we need it while developing,
but it's not something we want our users to install. We'll therefore put it
in a separate category of development-only requirements.

Add the following to your `pyproject.toml`:

```toml
[project.optional-dependencies]
dev = [
    "ruff",
]
```

!!! example "Install the new dependency"

    Run `python -m pip install .[dev]`

    This will install your core package along with the `dev` "extra".
    You should see that `pip` is searching for `ruff` and its dependencies.


## Run the linter and address issues

Now that it's installed, we can use the linter.

!!! example "Run the linter"

    Run `python -m ruff src` from the root of your project.
    
    Look at the error reported about an unused variable.
    The error is correctly identified, but the solution suggested is
    perhaps not the best... Address the error however you think is best,
    and rerun `ruff` to check that it reports no problems.
    

## Configure linting