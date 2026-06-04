import argparse
from pathlib import Path

from .findstrings import process_file

parser = argparse.ArgumentParser()

parser.add_argument("path", type=Path, help="Path to the file or directory")
parser.add_argument("--min-length", type=int, help="How many characters does a comment have to be before it's considered 'long'", default=50)

def main():
    args = parser.parse_args()
    p: Path = args.path
    if not p.exists():
        raise argparse.ArgumentError(None, f"Path {args.p} does not exist")
    
    if p.is_file():
        for res in process_file(p, min_length = args.min_length):
            print(res)
    elif p.is_dir():    
        # Walk through the directory tree
        for dirpath, dirnames, filenames in p.walk():        
            # Process files by joining the path object with the filename string
            for filename in filenames:
                if not filename.endswith('.py'): continue
                file_path = dirpath / filename
                for res in process_file(file_path, min_length = args.min_length):
                    print(res + "\n")
    else:
        raise argparse.ArgumentError(None, f"Path {args.p} is neither a file nor a directory")


if __name__ == "__main__":
    main()
