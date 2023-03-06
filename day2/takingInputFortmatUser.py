# # how to take from user & Type conversion
# num1=input("Enter first number:")
# num2=input("Enter second number:")
# # kullanıcıdan girişi alabileceğimiz bir işlevdir
# # num1 değişkeni oluşturuyorum, çalışma zamanında girfiğimiz değer ne olursa olsun bu değer num1 atanacak
#
# print(type(num1))   # <class 'str'>
# print(type(num2))   # <class 'str'>
# # girdi olarak sağladığımız değerler ne olursa olsun her şey bir dize (str) olarak kabul edilecek
#
# print(num1+num2)    # 100200
# # çünkü onları bir sayı olarak değil, bir dizi (str) olarak kabul ediyor
#
# # num1 ve num2 'yu sayı formatına dönüştürmeliyiz str 'ı int 'a dönüştürmeliyiz

# Approach 1
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
#
# print(type(num1))   # <class 'int'>
# print(type(num2))   # <class 'int'>
#
# print(num1+num2)    # 300

# Approach 2
# num1 =input("Enter first number:")
# num2 =input("Enter second number:")
#
# print(int(num1) + int(num2))  # 300

#Example 1
num1 =input("Enter first decimal number:")
num2 =input("Enter second decimal number:")
print(type(num1))   # str
print(type(num2))   # str

print(float(num1)+float(num2)) # 31.0

