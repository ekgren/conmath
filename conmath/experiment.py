import ast

from conmath.factory import ast_to_code, ast_to_string

# Create the AST for the function definition
function_def = ast.FunctionDef(
    name="add",
    args=ast.arguments(
        posonlyargs=[],
        args=[
            ast.arg(arg="x", annotation=None, lineno=1, col_offset=0),
            ast.arg(arg="y", annotation=None, lineno=1, col_offset=0),
        ],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[],
        lineno=1,
        col_offset=0,
    ),
    body=[
        ast.Assign(
            targets=[ast.Name(id="out", ctx=ast.Store(), lineno=1, col_offset=0)],
            value=ast.BinOp(
                left=ast.Name(id="x", ctx=ast.Load(), lineno=1, col_offset=0),
                op=ast.Add(),
                right=ast.Name(id="y", ctx=ast.Load(), lineno=1, col_offset=0),
                lineno=1,
                col_offset=0,
            ),
            lineno=1,
            col_offset=0,
        ),
        ast.Return(
            value=ast.Name(id="out", ctx=ast.Load(), lineno=1, col_offset=0),
            lineno=1,
            col_offset=0,
        ),
    ],
    decorator_list=[],
    returns=None,
    lineno=1,
    col_offset=0,
)

# Wrap the function definition in a Module node
module = ast.Module([function_def], type_ignores=[], lineno=1, col_offset=0)

# Compile the AST into a function
code = compile(module, "<string>", "exec")
print(ast.unparse(module))
exec(code)

# Test the function
print(add(["1"], ["2"]))  # Output: 3
