# name: cleanfilenames.py

import pathlib


def clean_file_names(include_non_py_files=False,
                     change_dashes=False,
                     change_spaces=False,
                     ):
    """Either change_dashes or change_spaces has to be True
    or a ValueError is raised.

    Setting include_non_py_files=True might result in unwanted behavior
    if both change_dashes and change_spaces are True.
    """
    if change_dashes is not True and change_spaces is not True:
        raise ValueError("change_dashes and change_spaces can't both be False")

    if include_non_py_files is True and change_dashes is True and change_spaces is True:
        if input("clean_file_name: All parameters have been set to True. "
                 "This might result in unwanted behavior."
                 "\n\nDo you want to continue? [y/N] ").casefold() != "y":
            print("Exiting...")
            return

    if include_non_py_files is True:
        filelist = pathlib.Path(".").glob("**/*")
    else:
        filelist = pathlib.Path(".").glob("**/*.py")

    for filename in filelist:
        if (
                ("Tidigare omgångars anteckningar" in filename.parts)
                or ("Tidigare omgångars övningar" in filename.parts)
                or ("venv" in filename.parts)
                ):
            continue

        if filename.is_file() and (" " in filename.name or "-" in filename.name):
            path_str = str(filename)
            new = path_str
            changed = False
            if " " in path_str and change_spaces:
                if changed is False:
                    print("Path:", filename)
                new = new.replace(" ", "_")
                print("New name:", new)
                changed = True
            if "-" in path_str and change_dashes:
                if changed is False:
                    print("Path:", filename)
                new = new.replace("-", "_")
                print("New name:", new)
                changed = True
            print()
            filename.rename(new)


def find_bad_files(include_non_py_files=False,
                   print_individual=False,
                   show_previous=False,
                   include_dashes=False,
                   include_spaces=False,
                   ):
    if include_dashes is not True and include_spaces is not True:
        print("find_bad_files: Both countable parameters have been set to False."
              " No files will be counted.")
        return
    if include_non_py_files:
        filelist = pathlib.Path(".").glob("**/*")
    else:
        filelist = pathlib.Path(".").glob("**/*.py")
    dirs = {}

    for filename in filelist:
        if (
                ("Tidigare omgångars anteckningar" in filename.parts)
                or ("Tidigare omgångars övningar" in filename.parts)
                or ("venv" in filename.parts)
                ) and show_previous is False:
            continue

        if " " in filename.name or "-" in filename.name:
            if filename.parent.name not in dirs:
                dirs[filename.parent.name] = {"-": 0, " ": 0}
            if print_individual:
                print("Path:", filename)

            if "-" in filename.name and include_dashes:
                dirs[filename.parent.name]["-"] += 1
                if print_individual:
                    print("Dash in Path:", filename)
            if " " in filename.name and include_spaces:
                dirs[filename.parent.name][" "] += 1
                if print_individual:
                    print("Space in Path:", filename)

    if len(dirs) < 1:
        print(f"No invalid files found in "
              f"/{pathlib.Path(".").absolute().parts[-1]}/ or any "
              f"sub-directories.")

    for k, v in dirs.items():
        print(k, v)


if __name__ == '__main__':
    print(f"Testing {find_bad_files.__name__} with "
          f"include_spaces = True, "
          f"include_dashes = True, "
          f"and include_non_py_files = True")
    find_bad_files(include_spaces = True, include_non_py_files = True)
