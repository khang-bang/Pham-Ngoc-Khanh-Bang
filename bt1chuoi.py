# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:04:39 2024

@author: HP
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
# tach sub_string 1
s1 = chuoi.split(", ")
for sub1 in s1:
    print(sub1)
# tach sub_tring 2
s2 = chuoi.replace("P. ","").replace("Q. ", "").replace("Tp. ", "")
s2 = s2.split(", ")
for sub2 in s2:
    print(sub2)