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
# str="welcome"
# print(str+" programming") # welcome programming
#
# print(str * 2) # welcomewelcome

#  Example4 : Sciling []
"""
dilimleme operatörünü kullanarak
- dizenin bir kısmını çıkarabilir
- dizedeki karakter sayısını bulabiliriz ve dizeyi alabilir veya dizeyi ters çevirebiliriz
dilimleme operatörlerini kullanarak dizeler üzerinde yapabiliceğimiz tüm işlemler
"""
# başlangıç indeksi her zaman 0'dan başlar
# bitiş indeksi her zaman 1'den başlar

# str="welcome"
# print(str[1:3]) # el
# print(str[:6]) # welcom here starting index is 0 by default
# print(str[2:]) # lcome
#
# print(str[1:-1]) # elcom last 1 char removed
# print(str[1:-2]) # elco lasr 2 chars removed
#
# # Example5 : ord() and chr()
#
# print(ord('A')) # 65 returns the ASCII code of the character
# print(chr(65)) # A returns character represented by a ASCII number

#Example6: max() min() len()
# print(max("abc")) # c
# print(min("abc")) # a
# print(len("abc")) # 3
#
# #Example7 : in ,  not in operators
# s="welcome"
# print("come" in s) # True
# print("lome" in s) # False
#
# print("come" not in s) # False
# print("lome" not in s) # True

# bu belirli dize ana dizenin bir parçasıysa, o zaman true değerini döndürür
# dizeyi kontrol eder ana dizede var olup olmadığına

#Example8 : String comparison (karşılaştırmak)
# dizileri karşılaştırmak çin ilişkisel operatörleri kullanabiliriz
# print("tim" == "tie")           #False
# print("free" != "freedom")      #True
# print("arrow" > "aron")         #True
# print("right" >= "left")        #True
# print("teeth" < "tee")          #False
# print("yellow" <= "fellow")     #False
# print("abc" > "")               #True

#Example9 : Testing strings True/False
# s="welcome to python"
# # bunun bir sayı olup olmadığını kontrol eder bu dize bir sayı içerip içermediğini
# print(s.isalnum()) # False
#
# # dize içerdiği şey alfabedir
# print("welco".isalpha()) # True
#
# # bu dizenin rakam içerip içermediğini doğrular, dizi rakam içeriyorsa True döndürür
# print("2012".isdigit()) # True
#
# # tanımlayıcı --> dizenin bazı anahtar kelimeleri içerip içermediğini anlamına gelir
# print("first Number".isidentifier()) # False
#
# # dizenin tüm küçük karakterleri içerip içermediğini kontrol eder
# print(s.islower()) # True
#
# # dize yalnızca büyük harfler içeriyorsa
# print("WELCOME".isupper()) # True
#
# #dize boşluk içeriyor yada içermiyorsa
# print(" ".isspace()) # True

# # Example10 :Searching for Substrings (alt dizeler)
# s="welcome to python"
#
# # tüm dize bu belirli dieyl biter
# print(s.endswith("thon")) # True
#
# # dize bu anahtar kelimeyle başlıyorsa veya bu dizeyle başlıyorsa true döndürür
# print(s.startswith("good")) # False
#
# # come ifadesini içeren değişken ana dizede mevcut olduğunu bulan ve tam olarak bulunduğu yerde pozisyonu geri getirecektir
# # yalnızca bir den başladı, come'ın tam olarak nerede olduğunu bulacaktır
# print(s.find("come")) # 3
#
# # anahtar kelime bulunamadığı için -1 döndürür
# print(s.find("become")) # -1 not found
#
# # bu t'nin dizede kaç kez tekrarlandığını sayar
# print(s.count("t")) # 2 returns number of occurrences of substring the string

#Example11 : Converting String
# s="String in PYTHON"
#
# s1=s.capitalize()
# print(s1) # String in python
#
# # her kelimenin büyük harfle başlayacağı anlamına gelir
# s2=s.title()
# print(s2) # String In Python
#
# s3=s.lower()
# print(s3) # string in python
#
# s4=s.upper()
# print(s4) # STRING IN PYTHON
#
# s5=s.swapcase()
# print(s5) # sTRING IN python
#
# s6=s.replace("in", "on")
# print(s6) # Strong on PYTHON

#Example12: Reverse a string
# Method1
# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print("reversed string is:",rev_str) # reversed string is: emoclew

#Method2
s="welcome"
rev_str=s[::-1]
print(rev_str) # emoclew