# Introduction

## The `pyproject.toml` file

Tools in the Python ecosystem have used a variety of formats to store their
configuration. More recently, `pyproject.toml` has emerged as a standardised
file that can specify information about a project itself,
as well as configuration options for various useful tools.

In this tutorial, we'll explore how to to use this file for packaging
a project and for customizing tools like linters and type checkers,
with the goal of improving the quality of a codebase.

## Learning goals

After completing this tutorial, you will be able to:

- interpret basic metadata for a project by looking at its `pyproject.toml`.
- specify dependencies and command-line entrypoints for your package.
- enable and configure linting and type-checking for a codebase.

## How to use this tutorial

The different chapters are intended to be followed in order.

If you are already familiar with tools like `ruff` and `mypy`,
you can skip to the [Appendix](appendix.md) after completing the
[Setting Up](setup.md) and [Packaging](packaging.md) chapters.

Sections that look like this:

!!! example "Try it out"

invite you to experiment. They have you see the effect
of the configuration you have built, and are a core part of the tutorial.

Sections that look like this:

!!! tip "Here's a tip"

contain more advanced suggestions.
You don't need to read or follow them to complete the tutorial.

Most chapters include a list of further resources at the end.
You can refer to these if you want more information on a specific topic,
although there will likely not be enough time to take them all in
during the tutorial.