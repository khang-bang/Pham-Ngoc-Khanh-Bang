# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:55:19 2024

@author: HP
"""
import math
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
bieu_thuc = ((math.sqrt(a) - math.sqrt(b))/(math.pow(a, 0.25) - math.pow(b, 0.25)))-((math.sqrt(a) + math.pow(a*b, 0.25))/(math.pow(a, 0.25) + math.pow(b, 0.25)))
print(bieu_thuc)