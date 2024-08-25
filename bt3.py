# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:21:08 2024

@author: Student
"""

N = int(input("Nhap so nguyen N: "))
if N > 9 and N < 100:
    a = N // 10
    b = N % 10
print("Tong 2 chu so cua N la: ", a + b)