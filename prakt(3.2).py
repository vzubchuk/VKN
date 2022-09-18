import sys
sideA=int(input("Перший катет трикутника a: "))
sideB=int(input("Другий катет трикутника b: ")) 
areaA= sideA * sideB / 2;
print("S=(a*b)/2:", areaA);
sideC=int(input("Висота призми h: "))
areaB= areaA * sideC;
print("V=S*h", areaB)