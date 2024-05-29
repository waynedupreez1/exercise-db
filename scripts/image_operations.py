"""Resize images and generate gifs

1. Resize images to width 600 and preserve aspect ratio
2. Create gifs

Author: Wayne du Preez 2024-05-29
"""

import os
import pathlib
import sys
import glob
from tqdm import tqdm
from PIL import Image

#Global Vars
IMAGE_DIR_NAME = "exercises"
IMAGE_WIDTH = 600

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

def resize_all_images(fullpath_image_name: str):
    """Resizes images

    Resize images to IMAGE_WIDTH and keep aspect ratio

    Args:
    fullpath_image_name: full path to image name

    Returns:
    None

    Raises:
    None
    """

    with Image.open(fullpath_image_name) as img:

        if img.width > IMAGE_WIDTH:
            wpercent = IMAGE_WIDTH / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((IMAGE_WIDTH, hsize), Image.LANCZOS)
            img.save(fullpath_image_name)
        else:
            print(f"image: {fullpath_image_name} width: {img.width} <= {IMAGE_WIDTH}")

def save_all_images_to_webp(fullpath_image_name: str):
    """Save images as webp

    Resave all the jpg images as webp

    Args:
    fullpath_image_name: full path to image name

    Returns:
    None

    Raises:
    None
    """
    fullpath_image_name_jpg = pathlib.Path(fullpath_image_name)
    fullpath_image_name_webp = fullpath_image_name_jpg.with_suffix(".webp")

    if fullpath_image_name_jpg.suffix == ".jpg":
        with Image.open(fullpath_image_name) as img:
            img.save(fullpath_image_name_webp, format="WEBP")

def create_gifs(fullpath_image_dir: str):
    """Generate gif's from jpg images

    Generate gifs from the images

    Args:
    fullpath_image_dir: full path to image dir

    Returns:
    None

    Raises:
    None
    """
    images = []

    glob_dir = os.path.join(fullpath_image_dir, "*.jpg")
    for infile in glob.glob(glob_dir):
        im = Image.open(infile)
        modified_img = im.quantize(colors=256, method=Image.MAXCOVERAGE, dither=0)
        images.append(modified_img)

    images[0].save(fp=os.path.join(fullpath_image_dir, "exercise.gif"), format='GIF', minimize_size=True,
                   append_images=images[1:], save_all=True, duration=1000, loop=0, all_mixed=True)

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

    parent_path = get_path_parent_dir()
    images_full_path = os.path.join(parent_path, IMAGE_DIR_NAME)
    list_of_image_dirs = get_list_dirs_or_files(images_full_path)

    for image_dir in tqdm(list_of_image_dirs):

        image_list = get_list_dirs_or_files(image_dir, list_dirs=False)

        for image in image_list:
            resize_all_images(image)
            #save_all_images_to_webp(image)

        create_gifs(image_dir)

if __name__ == "__main__":
    main()
