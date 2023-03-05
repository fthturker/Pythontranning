# Concatenation (birleştirme)  +
print(10+10)        # 20 valid
print(10.5+12.0)    # 22.5 valid
print(10+10.5)      # 20.5 valid

print("welcome " + "python")        # welcome python

print(True+ 5)      # 6
print(False+5)      # 5
print(True+True)    # 2
# True deyince değer olarak 1 alır False deyince değer olarak 0 alır

print(10+"welcome")     # Not valid bcoz 2 values are different type
print(10.5+"welcome")   # Not valid bcoz 2 values are different type
# TypeError: unsupported operand type(s) for +: 'int' and 'str' çıktısını alırız
print(True+"welcome")   # Not valid bcoz 2 values are different type

