#!/usr/bin/python3
import math

print("Теорема Пифагора - a²+b²=c²")
print("Введите a:")
a = float(input("a = "))
print("Введите b:")
b = float(input("b = "))

c = math.sqrt(a*a+b*b)
print(f"C равно {c}")
