# autoparse
Automatic Python Argument Parser from function signature and docstring

## usage
Define a function with type annotations, and use the autoparse decorator
as follows:

```python
# example.py
from autoparse import autoparse

@autoparse(verbose=True)
def example(a: str, b: int, c: float=1.0, d: bool=True) -> float:
    """
    Function signature with type annotations and docstring

    :param a: this is a required string parameter
    :param b: this is a required integer parameter
    :param c: this is an optional float parameter with a default value

    :return: doubles the value of the parameter c
    """
    return 2 * c

if __name__ == '__main__':
    example()
```
Now you can simply execute your python script and pass parameters directly on the command line
```bash
python example.py --a "hello" --b 2 --c 2.0 --d 0
```
Boolean values can be passed as integers (0=False, 1=True) or as a string
(['y', 't', 'true']=True, ['n', 'f', 'false']=False).

