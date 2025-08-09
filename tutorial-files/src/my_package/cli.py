from . import combine_arguments


def run():
    x = "A"
    y = "B"
    z = 4
    print(f"Trying out combine_arguments with {x=}, {y=}, {z=}")
    result = combine_arguments(x, y, z)
    print(f"Result is {result}")
