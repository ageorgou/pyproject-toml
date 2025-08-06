"""Main functionality for the package."""

def combine_arguments(x: str, y: str, z: int) -> str:
    """Build up a string from all 3 arguments."""
    return x + str(z)


def tokenize_input(input: str, token_length: int) -> list[str]:
    """Break down an input string into substrings of a given length."""
    if len(input) <= token_length:
        return input
    else:
        tokens = []
        start_index = 0
        while start_index < len(input):
            tokens.append(input[start_index:start_index + token_length])
            start_index += token_length


def process_file(filename: str):
    """Read a file and break down its contents.
    
    The first line contains the string to be tokenized. The second line
    contains the length of tokens to produce.
    """
    with open(filename, "r") as f:
        input_string = next(f)
        token_length = next(f)
    tokens = tokenize_input(input_string, token_length)
    