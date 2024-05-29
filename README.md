# Free Exercise DB [![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

Open Public Domain Exercise Dataset in `JSON` format

# What do they look like?

All exercises are stored as seperate `JSON` documents and conform to the following [JSON Schema](./schema.json) eg.

```json
{
  "id": "Alternate_Incline_Dumbbell_Curl",
  "name": "Alternate Incline Dumbbell Curl",
  "force": "pull",
  "level": "beginner",
  "mechanic": "isolation",
  "equipment": "dumbbell",
  "primaryMuscles": [
    "biceps"
  ],
  "secondaryMuscles": [
    "forearms"
  ],
  "instructions": [
    "Sit down on an incline bench with a dumbbell in each hand being held at arms length. Tip: Keep the elbows close to the torso.This will be your starting position.",
  ],
  "category": "strength",
  "images": [
    "Alternate_Incline_Dumbbell_Curl/0.jpg",
    "Alternate_Incline_Dumbbell_Curl/1.jpg"
  ]
}
```
See [Alternate_Incline_Dumbbell_Curl.json](./exercises/Alternate_Incline_Dumbbell_Curl.json)


## Incomplete fields

The following fields are incomplete in _some_ `JSON` files and in such have had to allow `null` in [schema.json](./schema.json)

* force
* mechanic
* equipment

## Images/Gifs

Converted All images to gifs
See Python Scripts

# Validation and checking

Validation of json files and checking it conforms to
the schema is done through pre-commit hooks

To use pre-commit hooks:

1. Install
> pip3 install pre-commit

2. Run in folder after clone
> pre-commit install

3. Run Agains all files
> pre-commit run --all-files

# Special Thanks
Forked from [here](https://github.com/yuhonas/free-exercise-db)
