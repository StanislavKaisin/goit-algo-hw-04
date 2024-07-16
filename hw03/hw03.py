import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_directory_tree(path: Path, indent: str = ""):

    if not path.is_dir():
        print(f"{Fore.RED}Error: '{path}' is not a directory or does not exist.")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
            print_directory_tree(item, indent + "\t")

        else:
            print(f"{Fore.MAGENTA}{indent}{item.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Missing argument: <directory_path>{Style.RESET_ALL}")
        return

    directory_path = Path(sys.argv[1])
    print("directory_path=", directory_path)

    if not directory_path.exists():
        print(f"{Fore.RED}Error: The path '{directory_path}' does not exist.")
        return

    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The path '{directory_path}' is not a directory.")
        return

    print(f"{Fore.GREEN}Directory tree of '{directory_path}':{Style.RESET_ALL}")
    print_directory_tree(directory_path)


if __name__ == "__main__":
    main()


# create virtual environment
# python -m venv .venv
# activate virtual environment
# source .venv/bin/activate
# install colorama
# pip install colorama
# generate file with installed dependencies
# pip freeze > requirements.txt
