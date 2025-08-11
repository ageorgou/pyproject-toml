# Type checking

Python is a dynamically-typed language and encourages
[duck-typing][duck-typing].
With this flexibility comes the risk of runtime errors due to unsupported
types, which can be hard to recover from and to replicate.

Type checkers analyse a codebase statically and can detect when types are used
inconsistently - for example, not respecting a function's type hints, or
combining values of different types in a way that is not guaranteed to work.
This can uncover potential bugs or edge cases where the code would fail
at runtime, but without needing to execute it.

Here we will use mypy, a static type checker, to further validate
our package's codebase.

## Install and run the type checker
Like with linters, a type checker is an optional dependency.

Modify `pyproject.toml` to  also install `mypy` as part of the `dev` extra:

```toml
[project.optional-dependencies]
dev = [
    "ruff",
    "mypy",
]
```

!!! example "Run mypy"

    Run `python -m pip install .[dev]`. Verify that `pip` now also installs
    the `mypy` package.


    Run `python -m mypy src`.

    Look at the errors for `library.py`. Compare the error messages to the
    type hints for the relevant functions, and try to understand why mypy
    is complaining.

    One error concerns an incorrect function invocation, while the others
    are bugs in the logic.
    The syntax is correct, the linter did not detect them,
    and the code may not have failed at runtime,
    but using the type checker has helped prevent them!

    Use the error messages to fix the problems.
    Rerun mypy and verify that no errors are reported.


## Configure mypy

Like with linters, mypy can be configured to be more or less strict,
and to ignore specific files.

To get the most thorough checks, you can specify the `strict` option.
This is useful once you have a type-safe codebase, but it may report
too many errors if you are still building up the code!

To enable this option, add a new section in `pyproject.toml`:

```toml
[tool.mypy]
strict = true
```

!!! example "Try the new configuration"

    Rerun mypy with `python -m mypy src`. You should now see more errors
    across two files.

    For `cli.py`, mypy is complaining about missing type annotations.
    This is something that it requires when run in strict mode.
    Add the annotation as the message suggests.

    For `experimental.py`, the errors reflect that the file is still being
    actively worked on. We could address them, but the code is likely to
    change. In this case, strict mode is perhaps inappropriate for this file.

    The easiest way around this is to tell mypy we don't want it to check
    anything in that file:

    ```toml
    [tool.mypy]
    ...
    exclude = ["experimental.py"]
    ```

    Rerun mypy to verify that errors for that file are not reported.


!!! tip "Per-module overrides"

    Mypy allows you to customise what options are applied to different files.
    For the example above, maybe you don't want to completely exclude
    `experimental.py`, but you also don't want to handle it in strict mode.
    Mypy lets you do this with an **override** for that file.

    To try this, remove the `exclude` option given above, and instead
    add another section:

    ```toml
    [[tool.mypy.overrides]]
    module = "my_package.experimental"
    disallow_untyped_defs = false
    warn_return_any = false
    ```
    (note the double brackets `[[...]]` in the section name!)

    This disables the two rules that were giving errors earlier,
    specifically for this module. Other rules still apply to it, and those
    two rules are still applied to other files.

    Run mypy again and confirm that there are no errors for `experimental.py`.



## Further resources

- The mypy docs have a lot of information, including an
[introduction to mypy and type-checking][mypy-getting-started]
and a detailed list of [available configuration options][mypy-config].
- [Pyright][pyright] is an alternative type checker.

[duck-typing]: https://docs.python.org/3/glossary.html#term-duck-typing
[mypy-getting-started]: https://mypy.readthedocs.io/en/stable/getting_started.html
[mypy-config]: https://mypy.readthedocs.io/en/stable/config_file.html#config-file-format
[pyright]: https://microsoft.github.io/pyright/#/