# name: cleanfilenames.py
"""
Functions:
- clean_file_names: Renames files based on user-provided options.
- find_bad_files: Identifies files with spaces or dashes in their names.
"""

import pathlib

IGNORED_DIRS = {
        "venv", ".venv", "env", ".env", "__pycache__",
        ".git", ".idea", ".vscode",
        }

PREVIOUS_COURSE_ROUNDS_DIRS = {
    "Tidigare omgångars anteckningar",
    "Tidigare omgångars övningar",
}

def _should_be_ignored(path, ignore_previous=True):
    """Checks if path should be skipped based on common patterns."""
    parts = set(path.parts)

    current_ignored = IGNORED_DIRS.copy()
    if ignore_previous:
        current_ignored.update(PREVIOUS_COURSE_ROUNDS_DIRS)

    if not parts.isdisjoint(current_ignored):
        return True
    if path.name.startswith("."):
        return True
    return False

def _get_files(include_non_py_files):
    """Returns a list of pathlib.Path objects."""
    glob_pattern = "**/*" if include_non_py_files else "**/*.py"
    return [path for path in pathlib.Path(".").glob(glob_pattern) if path.is_file()]

def _confirm_dangerous_operation():
    """Ensure user wants to continue with dangerous operation."""
    try:
        return input("clean_file_name: All parameters have been set to True. "
                     "This might result in unwanted behavior."
                     "\n\nDo you want to continue? [y/N] ").casefold() == "y"
    except EOFError:
        return False

def clean_file_names(include_non_py_files=False,
                     change_dashes=False,
                     change_spaces=False,
                     *,
                     force=False,
                     ):
    """Either change_dashes or change_spaces has to be True
    or a ValueError is raised.

    Setting include_non_py_files=True might result in unwanted behavior
    if both change_dashes and change_spaces are True.
    """
    if not (change_dashes or change_spaces):
        raise ValueError("change_dashes and change_spaces can't both be False")

    if all([include_non_py_files, change_dashes, change_spaces]) and not force:
        if not _confirm_dangerous_operation():
            print("Exiting...")
            return

    filelist = _get_files(include_non_py_files)
    skipped_files = {}

    for filename in filelist:
        if _should_be_ignored(filename):
            continue

        old_name = filename.name
        new_name = old_name
        if change_spaces:
            new_name = new_name.replace(" ", "_")
        if change_dashes:
            new_name = new_name.replace("-", "_")

        if new_name != old_name:
            print("\nPath:", filename)
            print("New name:", new_name)
            print()
            target_path = filename.with_name(new_name)
            if target_path.exists():
                print(f"File {target_path} already exists. Skipping...")
                skipped_files[filename] = target_path
            else:
                filename.rename(target_path)

    if skipped_files:
        print(f"\nSkipped {len(skipped_files)} files because targets existed:")
        for old, target in skipped_files.items():
            print(f"  {old} -> {target}")




def find_bad_files(include_non_py_files=False,
                   print_individual=False,
                   show_previous=False,
                   include_dashes=False,
                   include_spaces=False,
                   ):
    """Finds and reports files with dashes or spaces in their names.

    Either include_dashes or include_spaces has to be True
    or a ValueError is raised.

    Setting show_previous=True will include files from previous course rounds
    that are normally ignored.
    """
    if not (include_dashes or include_spaces):
        raise ValueError("find_bad_files: Both countable parameters have been set to False."
              " No files will be counted.")

    filelist = _get_files(include_non_py_files)
    dirs = {}

    for filename in filelist:
        if _should_be_ignored(filename, ignore_previous=not show_previous):
            continue

        has_space = " " in filename.name and include_spaces
        has_dash = "-" in filename.name and include_dashes

        if has_space or has_dash:
            parent_name = (str(filename.parent) if str(filename.parent) != "."
                           else "Current directory")
            if parent_name not in dirs:
                dirs[parent_name] = {"-": 0, " ": 0}
            if print_individual:
                # print()
                print("Path:", filename)

            if has_dash:
                dirs[parent_name]["-"] += 1
                if print_individual:
                    print(f"  Dash in Path:  {filename}")
            if has_space:
                dirs[parent_name][" "] += 1
                if print_individual:
                    print(f"  Space in Path: {filename}")

    print("\nProcessing complete.\n")

    if len(dirs) < 1:
        print(f"No invalid files found in "
              f"/{pathlib.Path('.').absolute().parts[-1]}/ or any "
              f"sub-directories.")

    else:
        print("Directories containing files with invalid names:")
        directories = dirs.items()
        for dir_name, counts in directories:
            print(f"{dir_name}:\n"
                  f"\tFiles with dashes: {counts['-']}\tFiles with spaces: {counts[' ']}")
                  # f"found {counts["-"]} files with names containing dashes and "
                  # f"{counts[" "]} files with names containing spaces.")
    print()


def main():
    print(f"Testing {find_bad_files.__name__} with "
          f"include_spaces = True, "
          f"include_dashes = True, "
          f"include_non_py_files = True, "
          f"and print_individual = False")
    find_bad_files(include_spaces=True, include_dashes=True, include_non_py_files=True,
                   print_individual=False)
    print("-" * 20)
    #clean_file_names(include_non_py_files=False, change_dashes=True, change_spaces=True)


if __name__ == '__main__':
    main()