# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 23:21:34 2021

@author: Dastur
"""

# ismlar = ["Ali", "Vali", "Odil", "Obit", "Sobit"] 
# i = 0
# for ism in ismlar:
#     print(f"Salom {ism}")
#     i += 1
# print(f"Kod {i} marta takrorlandi.")

# toq_sonlar = list(range(11, 100, 2))
# for toq_son in toq_sonlar:
#     print(f"{toq_son} ning ko'bi {toq_son ** 3} ga teng.")
    
# kinolar = []
# for k in range(5):
#     kinolar.append(input(f"{k+1}-sevimli filmizni kiriting->"))
    
# print(kinolar)

n = int(input("Bugun nechta odam bilan suhbatlashdingiz?\n"))
odamlar = []
for i in range(n):
    odamlar.append(input(f"{i+1}-suhbatlashgan odammingizni ismini kiriting->"))
print(odamlar)

    
