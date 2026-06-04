import io
from pathlib import Path
import tokenize
from typing import Generator, Callable


def debug(f: Callable) -> Callable:
    def inner(*args, **kwargs):
        print(f"Calling {f.__name__} with {args}")
        f(*args, **kwargs)
    return inner

def process_file(path: Path | str, min_length=100) -> Generator[str, None, None]:
    with open(path, "r") as f:
        src = f.read()

    yield from find_long_docstrings(src, min_length, filename=path)

def find_long_docstrings(source_code: str, min_length, filename: Path | str = "") -> Generator[str, None, None]:
    code_stream = io.StringIO(source_code).readline
    
    for token in tokenize.generate_tokens(code_stream):
        # Target string tokens starting with triple quotes
        if token.type == tokenize.STRING and token.string.startswith(('"""', "'''")):
            if len(token.string) >= min_length:
                yield construct_result_string(token.string, filename, token.start[0])

def construct_result_string(source: str, filename: Path | str, lineno: int) -> str:
    return f"{filename}({lineno}):\n{source}"

"""_summary_
This is a long string
"""