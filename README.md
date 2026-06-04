Find long comments and docstrings in a Python codebase.

In new and quickly-evovling projects, documentation often ends up in comments and docstrings rather than in formal docs. `longstrings` is a command line utility to find and emit these long comments for perusal.

## Usage

```sh
usage: longstrings.exe [-h] [--min-length MIN_LENGTH] path

positional arguments:
  path                  Path to the file or directory

options:
  -h, --help            show this help message and exit
  --min-length MIN_LENGTH
                        How many characters does a comment have to be before it's considered 'long'
```

## Examples

```sh
uvx longstrings ~/somefile.py
```

```sh
uvx longstrings ~/some_codebase/some_module --min-length 500
```
