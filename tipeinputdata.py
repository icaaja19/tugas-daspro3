# 2. input tipe data berbeda (string, integer, float)
a = str(input("string adalah :"))
b = int(input("integer adalah :"))
c = float(input("float adalah :"))

input_tipe_data = a, b, c

if isinstance (a, str) and isinstance (b, int) and isinstance (c, float):
    print("tipe data valid")
else:
    print("tipe tidak data valid")
    
    