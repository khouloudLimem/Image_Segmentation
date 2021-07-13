import os
from shutil import copy

import matplotlib.pyplot as plt
from PIL import Image


def delete_zero_images():
    image_folder = "C:\\Users\\dhiae\\Image_Segmentation\\DCGAN\\data\\masks"
    tumors = "C:\\Users\\dhiae\\Image_Segmentation\\DCGAN\\data\\Tumors"

    if not os.path.isdir(tumors):
        os.mkdir(tumors)

    for image_name in os.listdir(image_folder):
        img = Image.open(os.path.join(image_folder,image_name))

        if img.getextrema()[1] != 0:
            copy(os.path.join(image_folder, image_name), tumors)

delete_zero_images()