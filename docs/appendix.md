# Appendix: Converting existing configurations

The tools we have seen in the tutorial can read their configuration from
a variety of file formats.
Before `pyproject.toml` became standard, many projects used different files,
and some continue to do so.

This appendix has you migrate from older-style configurations to using
`pyproject.toml`. It also discusses some additional tools which were
not mentioned in the main tutorial.

The starter code comes with some sample configurations in the `old-configs`
directory.

## Packaging
The dependencies and other project metadata are provided in `setup.py`.
Move that to the `[project]` table of `pyproject.toml`.

The `setup.py` format is not deprecated, although commands like
`python setup.py install` and `python setup.py develop` are no longer favoured.
Instead, you should use `pip` to install a package from source.
PyPA has a [guide for modernizing `setup.py`-based projects][pypa-setup.py].

## Linting
Ruff uses TOML files for configuration (either its own `ruff.toml`
or `pyproject.toml`), but older linters look for a number of filenames.

Two sample configurations are provided in `pylintrc` and `.flake8`,
for Pylint and Flake8 respectively.

Pylint supports `pyproject.toml`, so you can recreate the same configuration
in that file.
On the other hand, Flake8 cannot be configured in `pyproject.toml`.
However, Ruff supports the whole set of Flake8 rules in
[its own rules][ruff-rules], so you can construct an equivalent configuration
for Ruff.

## Formatting
The black formatter can be configured only in `pyproject.toml`.

The isort utility can be configured with [various files][isort-config],
including `pyproject.toml` and `.isort.cfg` (as in the sample config).
The formats are very similar.

If using Ruff for linting, you may also want to use it for auto-formatting.
Currently, Ruff implements the isort rules under its linter, in the "I"
rules category. You can recreate the configuration from `.isort.cfg`
in Ruff, as indicated in its [docs][ruff-isort].


## Type checking
Mypy can store configuration in `pyproject.toml` or an ini file.
The two formats are very similar, with the main difference being the name
of the sections, particularly for overrides.
You should therefore be able to recreate the configuration from `mypy.ini`.

You can read more on the differences in the [mypy docs][mypy-toml],
which also contain an example `pyproject.toml`.

[pypa-setup.py]: https://packaging.python.org/en/latest/guides/modernize-setup-py-project/
[ruff-rules]: https://docs.astral.sh/ruff/rules/
[isort-config]: https://pycqa.github.io/isort/docs/configuration/config_files.html
[ruff-isort]: https://docs.astral.sh/ruff/formatter/#sorting-imports
[mypy-toml]: https://mypy.readthedocs.io/en/stable/config_file.html#using-a-pyproject-toml-file