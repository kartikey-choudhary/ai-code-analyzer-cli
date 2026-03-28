import ast


def extract_functions(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    tree = ast.parse(code)

    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # extract source code of function
            start_line = node.lineno - 1
            end_line = node.end_lineno

            func_source = "\n".join(code.splitlines()[start_line:end_line])

            functions.append({
                "name": node.name,
                "source": func_source
            })

    return functions