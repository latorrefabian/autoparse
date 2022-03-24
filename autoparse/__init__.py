import pdb
import inspect
import argparse

from docstring_parser import parse as doc_parse


def str_to_bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def autoparse(verbose=False):
    def autoparse_(fn):
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
            print('Running "' + fn.__name__ + '" with parameters ' + str(vars(args)))
        
        def fn_():
            return fn(**vars(args))

        return fn_

    return autoparse_
