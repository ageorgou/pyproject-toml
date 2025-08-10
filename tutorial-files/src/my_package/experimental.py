"""Some functions that are still being worked on."""

from typing import Any


def untyped(x):
    # TODO Process x and return something about it
    print(x)
    pass


def get_temp_value() -> Any:
    # This returns Any because I don't actually know what
    # it will be in reality
    return 5


def get_final_value() -> str:
    temp = get_temp_value()
    return temp
