from pathlib import Path

FILE_NAME = "salaries.txt"


def total_salary(filename: str) -> tuple[int, int]:
    script_path = Path(__file__).parent
    abs_file_path = script_path / filename
    try:
        with open(abs_file_path, "r", encoding="UTF-8") as f:
            data = f.readlines()
        total = 0
        count = 0

        for line in data:
            try:
                _, salary = line.strip().split(",")
                salary = int(salary)
                total = total + salary
                count = count + 1
            except ValueError as e:
                print(
                    f"ValueError: Could not convert line to an integer: {line.strip()}"
                )

        if count != 0:
            return total, total / count
        else:
            return (0, 0)

    except FileNotFoundError:
        print(f"FileNotFoundError: The file '{filename}' was not found.")
    except IOError:
        print(f"IOError: An error occurred while reading the file '{filename}'.")
    return (0, 0)


total, average = total_salary(FILE_NAME)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
