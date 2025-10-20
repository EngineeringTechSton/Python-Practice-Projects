# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 00:18:41 2025

@author: MALIK COMPUTERS
"""

import math
print("_______Area calculator:_______")
print("Select the object\n\nSquare:                1\nRectangle:             2\nCircle:                3\nTriangle(Height,Base): 4\nSphere:                5\nParallelogram:         6\nSector of Circle:      7\nArea of cylinder:      8")
choice=int(input("Choose:__"))
if choice==1:
    print("          Area of Square")
    side=float(input("Enter the side(length) of square: "))
    print(f"The Area of square is = {round((side*side),2)}")
elif choice == 2:
    print("          Area of Rectangle")
    length=float(input("Enter side 1 of Rectangle: "))
    width=float(input("Enter side 2 of Rectangle: "))
    print(f"The Area of Rectangle is = {round((length*width),2)}")
elif choice == 3:
    print("          Area of Circle")
    radi=float(input("Enter radius of circle: "))
    print(f"The Area of Circle is = {round((math.pi*radi),2)}")
elif choice == 4:
    print("          Area of Triangle")
    length=float(input("Enter height of triangle: "))
    width=float(input("Enter Base of triangle: "))
    print(f"The Area of Triangle is = {round(((1/2)*(length*width)),2)}")    
elif choice==5:
    print("          Surface Area of Sphere")
    radi=float(input("Enter radius of Sphere: "))
    print(f"The Surface Area of Sphere is = {round((4*math.pi*(radi**2)),2)}")
elif choice == 6:
    print("          Area of Parallelogram")
    length=float(input("Enter side 1 of Parallelogram: "))
    width=float(input("Enter side 2 of Parallelogram: "))
    print(f"The Area of Parallelogram is = {round((length*width),2)}")
elif choice == 7:
    print("          Area of Sector of Circle")
    radi=float(input("Enter radius of circle: "))
    print("Angle is in\nDegree:____1\nRadian____2\n")
    ang=int(input("Enter choice of angle: "))
    if ang==1:
        deg=int(input("Enter the angle in Degree:___"))
        print(f"The Area Sector of Circle is = {round(((deg/360)*math.pi*(radi**2)),2)}")
    elif ang==2:
        deg=int(input("Enter the Angle in radian:___"))
        print(f"The Area Sector of Circle is = {round(((1/2)*deg*(radi**2)),2)}")
    else:
        print("Invalid Choice:>>>>>>>>")        
elif choice ==8:
    print("Choose 1 or 2\n1:   Curved Surface area of cylinder\n2:   Total Surface Area of cylinder")
    ch8=int(input("(1 or 2)_____"))
    if ch8==1:
        print("____________Curved Surface Area of cylinder____________")
        h=float(input("Enter the hight of cylinder: "))
        radi=float(input("Enter radius of cylinder: "))
        print(f"The Curved Surface Area of Cylinder is = {round(((2)*math.pi*(radi*h)),2)}")
    elif ch8==2:
        print("____________Total Surface Area of cylinder____________")
        h=float(input("Enter the hight of cylinder: "))
        radi=float(input("Enter radius of cylinder: "))
        print(f"The Curved Surface Area of Cylinder is = {round((2)*math.pi*radi*(radi+h),2)}")
    else:
        print("Invalid Choice......")
else:
    print("Invalid Choice.......")
print("        💗Engr. Farhan Shakeel💻")
        
        
        
    
    
    
    
    
    