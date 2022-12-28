""" In factory we create AST objects programmatically and convert them to code. """
from typing import List, Optional, Type
import inspect
import ast


def create_ast_function(
    name: str,
    args: List[ast.arg],
    body: List[ast.stmt],
    decorator_list: List[ast.expr],
    returns: Optional[ast.expr],
) -> ast.FunctionDef:
    """Creates an AST FunctionDef object.
    https://docs.python.org/3/library/ast.html#ast.FunctionDef"""
    return ast.FunctionDef(
        name=name,
        args=ast.arguments(
            args=args,
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[],
        ),
        body=body,
        decorator_list=decorator_list,
        returns=returns,
    )


def string_to_ast(string: str) -> ast.AST:
    """Converts a string to an AST object.
    https://docs.python.org/3/library/ast.html#ast.parse"""
    return ast.parse(string)


def ast_to_string(ast_object: ast.AST) -> str:
    """Converts an AST object to a string.
    https://docs.python.org/3/library/ast.html#ast.dump"""
    return ast.dump(ast_object)


def ast_to_code(ast_object: ast.AST) -> str:
    """Converts an AST object to python code."""
    return ast.unparse(ast_object)


def test():
    code = """def test():\n    print("hello world")"""
    function = string_to_ast(code)
    print(code)
    print()
    print(ast_to_string(function))
    print()
    print(ast_to_code(function))


if __name__ == "__main__":
    test()
