"""json file operations

1. Append gif location to all json files
2. Rebuild main_excercise json

Author: Wayne du Preez 2024-05-30
"""


import os
import json
from tqdm import tqdm

import utils

#Global Vars
EXERCISE_JSON_DIR_NAME = "exercises"



def main():
    """Main function

    Main function that will run

    Args:
    None

    Returns:
    None

    Raises:
    None
    """

    parent_path = utils.get_path_parent_dir()
    exercise_json_full_path = os.path.join(parent_path, EXERCISE_JSON_DIR_NAME)
    exercise_json_files = utils.get_list_dirs_or_files(exercise_json_full_path, list_dirs=False)

    for json_file in tqdm(exercise_json_files):

        with open(json_file, mode="r", encoding="UTF8") as file:
            print(json_file)

            (json.load(file))

if __name__ == "__main__":
    main()
