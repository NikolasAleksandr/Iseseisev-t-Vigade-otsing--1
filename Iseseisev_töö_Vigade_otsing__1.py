#Iseseisev too "Vigade otsing -1"
from math import * #было написано не в том порядке
#В работе много где не хватало знаков *, было просто написано к примеру d=2r, а надо d=2*r
#В некоторых местах не хватало скобок
print("Ruudu karakteristikud")

a=float(input("Sisesta ruudu kylje pikkus => "))  # к input я добавил float ,потому что он преобразует значения в числа с плавающей запятой (везде к input я добавил float в этой работе)
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ymbermoot", P)
di=a*sqrt(2) #было написано math.sqr это неправильно
print("Ruudu diagonaal", round(di,2))
print()
print("Ristkyliku karakteristikud")
b=float(input("Sisesta ristkyliku 1. kylje pikkus => "))
c=float(input("Sisesta ristkyliku 2. kylje pikkus => "))
S=b*c
print("Ristkyliku pindala", S)
P=2*(b+c)
print("Ristkyliku ymbermoot", P)
di=sqrt(b**2+c**2) #было написано math.sqr это неправильно, также была * это умножение, а нам нужно возведение в степень
print("Ristkyliku diagonaal", round(di))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi labimoot", d)
S=pi*r**2 #было написано p() это неправильно
print("Ringi pindala", round(S, 2))
C=2*pi*r #было написано p() это неправильно
print("Ringjoone pikkus", round(C, 2))