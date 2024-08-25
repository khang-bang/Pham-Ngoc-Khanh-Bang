# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:11:59 2024

@author: Student
"""
import math
a = float(input(" Nhap so a: "))
b = float(input(" Nhap so b: "))
bieu_thuc = (math.sqrt(a) - math.sqrt(b))/(a**(1/4) - b**(1/4)) - (math.sqrt(a) + (a*b)**(1/4))/(a**(1/4) + b**(1/4))
print("Ket qua: ", bieu_thuc)