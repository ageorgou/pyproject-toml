# Linting

As codebases become larger, it is easier for mistakes to creep in.
**Linters** are tools that check the code for signs of potential problems,
like unused variables or uncommon usage patterns.

There are numerous linters for Python, and many of them can be configured
through `pyproject.toml`.
For this tutorial, we will use Ruff, a relatively recent suite of linters
and formatters tools, which draws inspiration from previous tools.


## Install the linter
Like many Python analysis tools, Ruff is available as a package we an install.

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

`ruff` uses a default set of rules when checking your code, but it can be
customized to add or remove from that rulset. This is useful when you want
to be stricter or, conversely, you want to ignore a particular rule.

Add the following section in `pyproject.toml`:

```toml
[tool.ruff.lint]
select = [
    "E",
    "F",
    "B",
    "SIM",
    "I",
    "ARG"
]
```

The above configuration specifies the set of rules to use.

!!! example "Try the new configuration"

    Rerun the linter. You should now seem some additional errors.

    Each error is accompanied by a code like `UP015`, indicating the rule
    it violates. The rules are grouped in categories starting with the
    same letter. For example, `I` indicates rules related to the ordering of
    imports, while `ARG` rules have to do with function arguments.
    With the above configuration, we have asked Ruff to check the categories
    `E`, `F` and so on.

    In our case, the additional category detected a bug: we are not using
    one of the function's arguments. Assuming this is unintentional,
    change the function body to fix the bug (use the `y` argument however
    you want).

    Rerun `ruff` to check that the errors are gone.


!!! tip "Exclude files from linting"

    Ruff will try to detect all relevant files to check, but sometimes
    you may want to exclude some files from it. For example, when you
    installed your package, `pip` may have created a `build` directory
    with a copy of your code. Running Ruff on those files will generally
    report the same errors as in `src`, which is redundant.

    We have been working around this by restricting the folder that `ruff`
    looks at through passing the extra command-line argument `src`,
    but it can be easier to configure this in `pyproject.toml`.

    Add the following entry in the file, below the previous configuration:
    ```toml
    [tool.ruff.lint]
    ...
    exclude = ["build/**"]
    ```

    Now you can simply run `python -m ruff check`, and the `build` diretory
    will be ignored. This also gives you finer-grained control, since
    you can exclude individual files.


## Further resources
- The Ruff documentation describes the different [rules][ruff-rules] you can
select from.
- It also explains how to [ignore a rule][ruff-ignore-rule], either entirely
or for individual lines or files.
- [Flake8][flake8] is another popular linter which can be customized
similarly.
- Ruff can also be used for [automatic formatting][ruff-format]
of your Python code, enforcing rules like line length and naming conventions.
Other formatters include [black][black] and [pycodestyle][pycodestyle].

[ruff-rules]: https://docs.astral.sh/ruff/rules/
[ruff-ignore-rule]: https://docs.astral.sh/ruff/linter/#error-suppression
[flake8]: https://flake8.pycqa.org/en/latest/index.html
[ruff-format]: https://docs.astral.sh/ruff/formatter/
[black]: https://black.readthedocs.io/en/stable/
[pycodestyle]: https://pycodestyle.pycqa.org/en/latest/