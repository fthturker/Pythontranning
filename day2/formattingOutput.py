# Formatting output (biçimlendirme çıktısı)
# konsol penceresinde bir şey yazdırmak istiyorsanız print işlevini kullanıyoruz
# konsolda bir şeyi çıktı olarak yazdırmak istiyorsak print deyimini kullanıyoruz ama istiyorum
# yazdırmak istediğim format ne olursa olsun sadece bu formatı değiştirmek istiyorum, böylece python'da çıktıyı
# biçimlendiren bir konseptimiz var

# name="john"
# age=30
# sal=5000.50

name, age, sal = "john", 30, 5000.50

# Approach 1
# print(name)
# print(age)
# print(sal)
#print(name,age,sal)

# Approach 2
#Name is john
#Age is 30
#Sal is 5000.5
# print("Name is", name)
# print("Age is", age)
# print("Sal is", sal)

# Approach 3
#print("Name is:%s \nAge is:%d\nSalary is:%g"   %(name,age,sal))

# Approach 4  {}
print("Name is:{}\nAge is:{}\nSalary is:{}"  .format(name,age,sal))



