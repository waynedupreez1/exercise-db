"""json file operations

1. Append gif location to all json files
2. Rebuild main_excercise json

Author: Wayne du Preez 2024-05-30
"""


import os
import json
import pathlib
from tqdm import tqdm
from jsonschema import validate

import utils

#Global Vars
EXERCISE_JSON_DIR_NAME = "exercises"

def rebuild_all_json_file(list_exercise_full_path_json: list[str]):
    """rebuild all json file

    Rebuilds the file that contains all of the exercises

    Args:
    list_exercise_full_path_json: list of all the exercise file paths

    Returns:
    None

    Raises:
    None
    """
    all_exercise_data = {
        "all": []
    }

    parent_path = utils.get_path_parent_dir()
    all_json_file = os.path.join(parent_path, "all.json")

    for exercise_file_path in list_exercise_full_path_json:

        with open(exercise_file_path, mode="r", encoding="UTF8") as exercise_file:
            data = json.load(exercise_file)
            all_exercise_data["all"].append(data)

    with open(all_json_file, mode="w", encoding="UTF8") as all_json:
        all_json.write(json.dumps(all_exercise_data, indent=4))


def validate_against_schema(fullpath_exercise_json_name: str):
    """Validate instance against schema

    This validates the instance against the schema

    Args:
    fullpath_exercise_json_name: full path to exercise json name
    fullpath_json_schema_name: full path to schema json name

    Returns:
    None

    Raises:
    None
    """
    parent_path = utils.get_path_parent_dir()
    schema_path = os.path.join(parent_path, "schema.json")

    with open(fullpath_exercise_json_name, mode="r", encoding="UTF8") as instance_file:
        with open(schema_path, mode="r", encoding="UTF8") as schema_file:

            instance = json.load(instance_file)
            schema = json.load(schema_file)

            validate(instance=instance, schema=schema)

def append_gif_json_object(fullpath_exercise_json_name: str):
    """append gif object

    Apends the json gif object to the json file

    Args:
    fullpath_exercise_json_name: full path to exercise json name

    Returns:
    None

    Raises:
    None
    """
    path_obj = pathlib.Path(fullpath_exercise_json_name)
    file_name = path_obj.stem
    print(file_name)

    with open(fullpath_exercise_json_name, mode="r", encoding="UTF8") as read_file:

        data = json.load(read_file)

        #Check if gif objects exists:
        if "gif" not in data:
            data["gif"] = f"{file_name}/exercise.gif"

            with open(fullpath_exercise_json_name, mode="w", encoding="UTF8") as write_file:
                write_file.write(json.dumps(data, indent=4))
        else:
            print(f"gif object already in file: {fullpath_exercise_json_name}")

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
        append_gif_json_object(json_file)
        validate_against_schema(json_file)

    rebuild_all_json_file(exercise_json_files)

if __name__ == "__main__":
    main()
