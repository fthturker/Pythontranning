# create string varaible

# Example 1 ways of creating string variables
# s="welcome"
# s='welcome'
# s=str("welcome")
# s=str('welcome')

# creating empty string variables
# name=""
# name=''
# name=str()

# Example 2  ways of creating string variables
# mutable ->  cannot change the value of variable
# immutable -> can change the value of the variable
# string is immutable

# str1="welcome"
# print(id(str1)) # 2364237149616
#
# str1=str1+" to python"
# print(str1) # welcome to python
# print(id(str1)) # 1609028948240

# if the value is changed after updation then it is immutable
# aynı değişkeni tekrar tekrar kullanırsam bellek konumu değiştirilecek farklı kimlikler oluşturulacak
# diziler değişmezdir(immutable)

# Example 3  + and * with string
str="welcome"
print(str+" programming") # welcome programming

print(str * 2) # welcomewelcome
