# 3. input pengunaan untuk dua nilai : x dan y
x = int(input("masukan nilai x :"))
y = int(input("masukan niai y :"))

bool_x = bool (x)
bool_y = bool (y)

print(f"\nHasil konversi: x = {bool_x},y = {bool_y}\n")
print(f"x AND y : {bool_x} and {bool_y}")
print(f"x OR y : {bool_x} or {bool_y}")
print(f"NOT x : {not bool_x}")
print(f"x XOR y : {bool_x} != {bool_y}")
