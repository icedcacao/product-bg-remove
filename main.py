from PIL import Image
from typing import Dict
import os
from rembg import remove


def load_images_from_folder(folder):
    images = {}
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        if img is not None:
            images[filename] = img
    return images

def remove_background(img):
    result = remove(img)
    return result

def trim_transparent(img):
    result = img.crop(img.getbbox())
    return result


def main(): 
    input_folder = "input"
    output_folder = "output"
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    images = load_images_from_folder(input_folder)
    for key, value in images.items():
        s1 = remove_background(value)
        s2 = trim_transparent(s1)
        output_filename = key.split(".")[0]
        s2.save(os.path.join(output_folder, output_filename + ".png"))

if __name__ == "__main__":
    main()



