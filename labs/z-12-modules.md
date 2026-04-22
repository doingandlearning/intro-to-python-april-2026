# Lab 12: Modules and Imports with `os`

This lab focuses on splitting code into modules and importing functions in a main program.

You will practise:

- creating a helper module
- importing functions into another file
- using common `os` directory operations
- checking simple filesystem conditions before actions

---

## Hints and Tips

- Keep `file_utils.py` focused on helper functions only.
- Keep `main.py` focused on user interaction and menu flow.
- Return messages from helper functions instead of printing inside them.
- Use `os.path.exists(...)` before create/delete/rename actions.
- Test one menu option at a time.

---

## Task 1: Set Up the Module Files

Create a folder named `file_manager_lab` with two files:

1. `file_utils.py`
2. `main.py`

Goal:

- `file_utils.py` will contain filesystem helper functions.
- `main.py` will import and use those helpers.

---

## Task 2: Write Helper Functions in `file_utils.py`

In `file_utils.py`, write these functions:

1. `get_current_directory()`
2. `list_files(directory)`
3. `create_directory(directory_name)`
4. `delete_directory(directory_name)`

Rules:

- Use the `os` module.
- Use `if` checks (for example `os.path.exists(...)`) before actions.
- Return readable strings for success/failure.

<details>
<summary>Solution (Task 2)</summary>

```python
import os


def get_current_directory():
    return os.getcwd()


def list_files(directory):
    if not os.path.exists(directory):
        return "Directory not found."
    return os.listdir(directory)


def create_directory(directory_name):
    if os.path.exists(directory_name):
        return "Directory already exists."
    os.mkdir(directory_name)
    return f"Directory '{directory_name}' created successfully."


def delete_directory(directory_name):
    if not os.path.exists(directory_name):
        return "Directory not found."
    if len(os.listdir(directory_name)) > 0:
        return "Directory is not empty or cannot be deleted."
    os.rmdir(directory_name)
    return f"Directory '{directory_name}' deleted successfully."
```

</details>

---

## Task 3: Use Imports in `main.py`

In `main.py`, import the helpers from `file_utils.py`.

Build a looped menu with options:

1. Show current directory
2. List files in a directory
3. Create a directory
4. Delete a directory
5. Exit

<details>
<summary>Solution (Task 3)</summary>

```python
from file_utils import (
    get_current_directory,
    list_files,
    create_directory,
    delete_directory,
)


def main():
    while True:
        print("\nFile Manager")
        print("1. Show current directory")
        print("2. List files in directory")
        print("3. Create a new directory")
        print("4. Delete a directory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Directory:", get_current_directory())
        elif choice == "2":
            directory = input("Enter directory to list files: ")
            print("Files:", list_files(directory))
        elif choice == "3":
            directory_name = input("Enter new directory name: ")
            print(create_directory(directory_name))
        elif choice == "4":
            directory_name = input("Enter directory name to delete: ")
            print(delete_directory(directory_name))
        elif choice == "5":
            print("Exiting the File Manager.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
```

</details>

---

## Task 4 (Optional): Add a Rename Function

In `file_utils.py`, add:

`rename_directory(old_name, new_name)`

Rules:

1. Use `os.rename(...)`.
2. Return a success message when rename works.
3. Return a clear error message if the source directory does not exist.
4. Return a clear error message if the target directory name already exists.

Then add a new menu option in `main.py` to call this function.

<details>
<summary>Solution (Task 4 Optional)</summary>

```python
import os


def rename_directory(old_name, new_name):
    if not os.path.exists(old_name):
        return "Source directory not found."
    if os.path.exists(new_name):
        return "Target directory already exists."
    os.rename(old_name, new_name)
    return f"Directory '{old_name}' renamed to '{new_name}'."
```

</details>

---

## Reflection

- Why is splitting code between `file_utils.py` and `main.py` useful?
- What did `import` make easier in this lab?
- Which `if` checks helped prevent mistakes before filesystem actions?
