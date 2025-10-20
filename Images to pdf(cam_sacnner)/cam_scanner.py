# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 20:34:42 2025

@author: Farhan Shakeel
"""


#_______________________________Cam Scanner ______________________________________________________

import img2pdf
import os

os.chdir(r"C:\\Users\\Farhan Shakeel\\Desktop\\Resized_images")
print(os.getcwd())
img_folder = os.listdir("C:\\Users\\Farhan Shakeel\\Desktop\\Resized_images")  # path of folder in which images are present 



i=0
img_lis = []
for i in range(len(img_folder)):
    if img_folder[i].endswith((".jpeg",".png",".jpg")):
        img_lis.append(img_folder[i])
        i+=1
    else:
        continue
       
with open("output_8.pdf","wb") as file:
    layout = img2pdf.get_layout_fun(pagesize=(600,850)) # perfect
    file.write(img2pdf.convert(img_lis,layout_fun=layout))
    print("✅ PDF created succesfully 👍")    
    
        
        
        
        

