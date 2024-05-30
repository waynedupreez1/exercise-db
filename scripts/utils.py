"""Common Utilities

Contains common utilities

Author: Wayne du Preez 2024-05-29
"""

import os
import pathlib
import sys

def get_list_dirs_or_files(path: str, list_dirs:bool = True) -> list[str]:
    """Return elist of dirs or list of files

    This will list all dirs or all files depending on list_dirs

    Args:
    path: The path to the directory to check
    list_dirs: If true return dirs if false return files

    Returns:
    List of dirs or files

    Raises:
    None
    """

    if list_dirs:
        return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_path_parent_dir():
    """Return a parent directory

    This function should return the full path for a directory
    from this directory

    Args:
    dir_name: Directory name we want the full path to

    Returns:
    Full path of a parent directory

    Raises:
    None
    """
    path = pathlib.Path(__file__).parents[1]

    #Check if path exists
    if path.exists():
        return str(path)

    print(f"Path {path} does not exist")
    sys.exit(1)
