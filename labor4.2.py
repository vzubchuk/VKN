import math
x=int(input("Введіть X= "))
y=int(input("Введіть Y= "))
a=int(input("Введіть a= "))
t=int(input("Введіть t= "))
Z=2,33*math.pi*(x*math.sin(y)+y*math.cos(a))+(math.e**a*t)
print(Z)