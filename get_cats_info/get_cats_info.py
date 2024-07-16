from pathlib import Path

FILE_NAME = "cats_file.txt"


def get_cats_info(filename: str) -> tuple[int, int]:
    script_path = Path(__file__).parent
    abs_file_path = script_path / filename
    cats = []
    try:
        with open(abs_file_path, "r", encoding="UTF-8") as f:
            data = f.readlines()
        for line in data:
            (id, name, age) = line.strip().split(",")
            cat = {}
            cat["id"] = id
            cat["name"] = name
            cat["age"] = age
            cats.append(cat)

    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{filename}' was not found.")
    except IOError:
        print(f"IOError: An error occurred while reading the file '{filename}'.")
    return cats


cats_info = get_cats_info(FILE_NAME)
print(cats_info)
