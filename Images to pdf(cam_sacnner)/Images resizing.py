# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 14:14:06 2025

@author: Farhan Shakeel
"""

#_______________ Resizing _________________________ to A4
from PIL import Image
import os

os.chdir(r"G:\\youtube channel video")
# 📂 Folder containing your images
input_folder = "New folder"          # change to your folder name
output_folder = "Resized_images" # output folder

# 📏 Desired size (width, height)
new_size = (1785, 2526)

# ✅ Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 📸 Loop through all files in folder
for i in os.listdir(input_folder):
    if i.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        img_path = os.path.join(input_folder, i)
        print(img_path,"____________________________")
        img = Image.open(img_path)

        # ✂️ Resize the image
        img_resized = img.resize(new_size)

        # 💾 Save the resized image
        save_path = os.path.join(output_folder, i)
        img_resized.save(save_path)

        print(f"✅ Resized: {i}")

    