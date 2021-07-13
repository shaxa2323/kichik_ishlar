# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 10:53:03 2021

@author: Dastur
"""

# names = ["Sherbek", "Xolmurod", "Jasur"]
# xabar1 = f"Salom {names[0]} bugun diskotekaga boramizmi?"
# xabar2 = f"{names[1]} nimalar qilayapsiz?"
# xabar3 = f"Sog'misan {names[2]}?"
# print(xabar1)
# print(xabar2)
# print(xabar3)

# numbers = [1, 2, 12.03, -78, -4.45]
# print(numbers)
# numbers[1] = 5
# n = numbers[2] 
# numbers[2] = numbers[4]
# numbers[4] = n
# print(numbers)

# t_shaxslar = ["Alparslon", "Ibni Kasir"]
# z_shaxslar = ["Mubashir Ahmad", "Zakir Nayk"]
# print(f"Men tarixiy shaxslardan {t_shaxslar[0]} bilan zamonaviy shaxslardan {z_shaxslar[1]} bilan suxbat qilishni istardim.")

friends = ["Sherbek", "Dilbek", "Jasur", "Baxtiyor", "Ruzmurod"]
print(friends)
friends.remove("Ruzmurod")
friends.insert(0,"Doston")
friends.append("Raxim")
friends.insert(3,"Muslim")
print(friends)
mexmonlar = []
mexmonlar.append(friends.pop(0))
mexmonlar.append(friends.pop(1))
mexmonlar.append(friends.pop(2))

print(mexmonlar)
