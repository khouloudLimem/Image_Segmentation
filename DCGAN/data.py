import os
import shutil
import re

import config as config

conf = config.Config()


target_dir = 'C:\\Users\\khoul\\Documents\\PyTorch-GAN\\implementations\\gan\\src\\data\\masks'
file_extension = "(?<=mask).tif$"

for folder in os.listdir(conf.KAGGLE_3M_DATASET_DIR):
    folder_path = os.path.join(conf.KAGGLE_3M_DATASET_DIR, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if re.search(file_extension, file):
                shutil.copy(os.path.join(folder_path, file), target_dir)



    