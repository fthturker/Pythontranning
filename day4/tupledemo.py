# Tuple (demet)
"""
1- A tuple is a collection which is ordered and unchangeable
bir demet sıralı ve değişmez bir koleksiyondur.
2- In python tuples are written with round brackets.
python demetleri yuvarlak parantezlerle yazılır --> ()
3- Tuple is ımmutable.
bir demet değişmezdir
"""
#Example1: creating tuple
# mytuple=("apple","banana","cherry")
# print(mytuple) # ('apple', 'banana', 'cherry')

# mytuple=() # boş demet empty tuple

#Example2 : access tuple items
# mytuple=("apple","banana","cherry")
# print(mytuple[0]) # apple  here index starts drom 0
# print(mytuple[1]) # banana
# print(mytuple[2]) # cherry
# print(mytuple[-1]) # cherry

#Example3: range of indexes
# mytuple=("apple","banana","cherry","orange","kiwi","melon","mango")
# print(mytuple[2:5]) # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1]) # ('orange', 'kiwi', 'melon')

#Example4: Changing tuple items
"""
if it is Immutable below things are not possible...
1- we cannot modify existing value
mevcut olanı değiştiremeyiz
2- we cannot append new value
değere yeni değer ekleyemiyoruz
3- we cannot insert a new value

4- we cannot remove a value
mevcut değeri kaldıramıyoruz

ne zaman değişmez dediğimde bu dört seçenek uygulanabilir çünkü liste durumunda liste değişmezdir
dediğimde bu dört seçenek uygulanabilir çünkü liste durumunda liste değişmezdir bu yüzden yapabiliyoruz
tüm bu işlemleri liste değişgeninde yapmak için, ancak tuple sabit bir nesne olduğu için bu işlemleri 
tuple üzerinde gerçekleştiremiyoruz,
"""
"""
-- by default tuple does not allow you change values booz it is immutable
böylece deöet öğelerini varsayılan olarak değiştirerek varsayılan değişmez olduğu için değerleri değiştirmenize izin 
vermez bu varsayılan olarak Tuple sabit olduğu için değerleri değiştirmenize izin vermez,
ama dolaylı yoldan bir geçici çözüm var, bunu yapabiliriz,
-- but there is work around
bu tuple'ı listeye dönüştürüp bazı değişiklikler yapıp tekrar o listeyi demet'e çevirebiliriz
"""
# #Tuple --> list(modify) --> tuple
# mytuple=("apple","banana","cherry")
#
# mylist=list(mytuple)
# mylist[0]="orange"
#
# mytuple=tuple(mylist)
# print(mytuple)  # ('orange', 'banana', 'cherry')

#Example5: readig tuple items using loop
# mytuple=("apple","banana","cherry")
# for i in mytuple:
#     print(i)

#Example6: Check if Item Exists(searching of item in tuple)
# bir öğenin çiftte var olup olmadığını kontrol etmek istiyorum, öğenin içinde olup olmadığını kontrol etmek istiyorum
# demet olup olmadığını nasıl kontrol edebiliriz,
# mytuple=("apple","banana","cherry")
# if "banana" in mytuple:
#     print("yes, banana is present")
# else:
#     print("no, banana is not present") # yes, banana is present

#Example7: Tuple length - counting items in a tuple
# #bir demetteki topla öğe sayısını bulun
# mytuple=("apple","banana","cherry")
# print(len(mytuple))  # 3

#Example8: add items to tuple - not possible bcaz tuple is immutable - cannot change values/items
#öğeyi demetn içine ekle  -- ekleyemeyiz çükü tuple immutable dır
# mytuple=("apple","banana","cherry")
# mytuple[0]="orange"
# print(mytuple) # TypeError: 'tuple' object does not support item assignment

#Example9: copy tuple
# bir demeti başka bir demete kopyalayabiliriz çünkü verilerdeki hiçbir şeyi doğrudan değiştirmiyoruz
# mytuple1=("apple","banana","cherry")
# mytuple2=mytuple1
# print(mytuple2) # ('apple', 'banana', 'cherry')

#Example10: removing items from tuple
# tuple'dan öğeleri kaldırmak istiyorum demetten öğeleri kaldırmak mümkün değil --> çünkü tuple değişmez
# mytuple=("apple","banana","cherry")
# # mytuple.remove("apple")  # invalid/ it is not possible
# del mytuple
# print(mytuple) # NameError: name 'mytuple' is not defined. Did you mean: 'tuple'?

#Example11:  Join/combine tuple   (birleştirmek)
# tuple1=(10,20,30)
# tuple2=("a","b","c")
#
# tuple3=tuple1+tuple2
# print(tuple3) # (10, 20, 30, 'a', 'b', 'c')

#Example12: tuples comparison
# tuple1=(10,20,30)
# tuple2=("a","b","c")
#
# if tuple1==tuple2:
#     print("tuples are equal")
# else:
#     print("tuples not are equal") # tuples not are equal

