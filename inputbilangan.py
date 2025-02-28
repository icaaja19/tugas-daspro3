# 1. Menerima 3 input bilangan bulat : a, b, c.
a = int(input("Masukan bilangan a :"))
b = int(input("Masukan bilangan b :"))
c = int(input("Masukan bilangan c :"))

if (a >= b or b >= c) and (a % 2 == 0) and (c % 2 != 0) and ( b != c):
    print("Kondisi terpenuhi")
else :
    print("Kondisi tidak terpenuhi")

