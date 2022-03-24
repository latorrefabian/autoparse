from autoparse import autoparse


@autoparse()
def example(a: str, b: int, c: float=1.0, d: bool=True) -> float:
    """
    Function signature with type annotations and docstring

    :param a: this is a required string parameter
    :param b: this is a required integer parameter
    :param c: this is an optional float parameter with a default value
    :param d: this is an optional boolean parameter with a default value

    :return: doubles the value of the parameter c
    """
    return 2 * c


if __name__ == '__main__':
    example()
