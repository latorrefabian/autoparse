import inspect
import argparse

from docstring_parser import parse as doc_parse
from typing import Callable


def str_to_bool(v: str) -> bool:
    """
    Transform a string to a boolean value

    :param v: string to be transformed
    
    :return: boolean value according to the meaning of the parameter v
    """
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def autoparse(fn: Callable, verbose: bool=False) -> dict:
    """
    Parse parameters from the command line, according to the signature and
    docstring of a function

    :param fn: callable with type hints and docstring
    :param verbose: if True, will print the arguments parsed

    :return: dictionary containing the parameter names and values
    """
    signature = inspect.signature(fn)
    docs = doc_parse(fn.__doc__)
    param_desc = {p.arg_name: p.description for p in docs.params}
    parser = argparse.ArgumentParser(docs.short_description)

    for name, param in signature.parameters.items():
        required = param.default is inspect._empty

        if param.annotation is bool:
            type = str_to_bool
        else:
            type = param.annotation

        if name in param_desc.keys():
            help = param_desc[name]
        else:
            help = None

        parser.add_argument(
                    '--' + name, type=type,
                    required=required, help=help)

        if not required:
            parser.set_defaults(**{name: param.default})

    args = parser.parse_args()

    if verbose:
        print('Running "' + fn.__name__ + '" with parameters:')
        for key, value in vars(args).items():
            print('    -', str(key) + ':', value)

    return vars(args)
