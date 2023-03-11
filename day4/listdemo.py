# #Example1 : how to create list
# # python'da bir  liste nasıl oluşturulur
# # ilk önce yapacağımız şey önce bir değişken oluşturmak
# # liste farklı veri türleri depolamamıza izin verir
# mylist1=[10,20,30,40,50,20.5]
# mylist2=["apple","banana","cherry"]
# mylist3=["apple",20,"banana",50]
# mylist=list()   # empty list
#
# print(mylist1)  # [10, 20, 30, 40, 50, 20.5]
# print(mylist2)  # ['apple', 'banana', 'cherry']
# print(mylist3)  # ['apple', 20, 'banana', 50]
# print(mylist)   # []

#Example2 : Accessing items from the list
# şimdi öğelere nasıl erişeceğimizi göreceğiz
# aşağıdaki öğelere ayrı ayrı erişmek istiyorum
# listedeki her öğe listedeki indeks numarası ile temsil edilir
# indeks numarası her zaman 0 dan başlar
# mylist=["apple","banana","cherry"]  # index starts from zero
# print(mylist[0]) # apple
# print(mylist[1]) # banana
# print(mylist[2]) # cherry
# print(mylist[-1]) # cherry ---> elemanı sondan sayacak

#Example3 : Range of indexes (indeks aralğı)
# mylist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(mylist[2:5]) # ['cherry', 'orange', 'kiwi']
# # 2 başlangıç elemanıdır 5 bitiş elemanıdır yani 2 dahil 5 dahil değildir
# print(mylist[-4:-1]) # ['orange', 'kiwi', 'melon']

#Example4 : change item values
# mylist=["apple","banana","cherry"]
# print(mylist) # ['apple', 'banana', 'cherry']
# # ilk öğeyi değiştirmek istiyorum
# mylist[0]="orange"
# print(mylist) # ['orange', 'banana', 'cherry']

#Example5: read the items using loop  (öğeleri nasıl okuyacağız loop deyimini kullanarak)
# mylist=["apple","banana","cherry"]
# for i in mylist:
#     print(i)

#Example6 : check if the item is exist in the list or not
# mylist=["apple","banana","cherry"]
# # apple 'ın bu listede olup olmadığını kontrol etmek istiyorum
# if "apple" in mylist:
#     print("yes, apple is present") # yes, apple is present
# else:
#     print("no, apple is not present")

#Example7 : list length (counting number of items in a list)
# listenin uzunluğunu bulmak istiyorum. listedeki toplam öğe sayısını bulmak istiuorum.
# mylist=["apple","banana","cherry"]
# print(len(mylist))  # 3

#Example8 : Add items
"""
listeye yeni bir öğe eklemek istiyorum. eklemek için öğeler listeye yeni bir öğe var.
iki fonksiyonumuz var
1-) append()
2-) insert()
"""
# mylist=["apple","banana","cherry"]
# #mylist.append("orange")
# #print(mylist)  # ['apple', 'banana', 'cherry', 'orange']
# # yeni eklenen öğe listenin sonuna eklenir
# # listenin ortasına bir yere bir değer eklemek istediğimi varsayalım
# # insert kullandığımda öğeyi tam olarak nereye eklediğimizi söylememiz gerekiyor
# # böylece bunun için dizini de belirtmemiz gerekiyor indeks virgül öğe değeri
# mylist.insert(1,"orange") # add item some where in the middle of the list based on the index
# print(mylist) # ['apple', 'orange', 'banana', 'cherry']

#Example9 : remove item from the list
"""
öğeyi listeden çıkarmak istiyorum
üç yöntem var
1- pop()
2- del
del tam olarak işlev değil aslında bu bir anahtar kelime yani del tam olarak fonksiyon değil 
ve anahtar kelime ile fonksiyon arasındaki fark nedir,
eğer bir fonksiyon ise, () parantezlerimiz var ve anahtar bir kelime varsa sadece del olarak kullanmalıyız
3- clear()
listedeki tek bir öğeyi değil, listedeki tüm öğeleri temizleyecek
"""
# mylist=["apple","banana","cherry"]
# mylist.pop(0) # here we should specify index not the value
# print(mylist) # ['banana', 'cherry']

# mylist=["apple","banana","cherry"]
# del mylist[2] # here del command removes single item based on the index
# print(mylist) # ['apple', 'banana']

# mylist=["apple","banana","cherry"]
# mylist.clear()
# print(mylist) # []

#Example10 : copy list kopyalama listesi
# list()
# mylist1=["apple","banana","cherry"]
# mylist2=list(mylist1)
# print(mylist1) # ['apple', 'banana', 'cherry']
# print(mylist2) # ['apple', 'banana', 'cherry']

#copy()
mylist1=["apple","banana","cherry"]
mylist2=mylist1.copy()
print(mylist1) # ['apple', 'banana', 'cherry']
print(mylist2) # ['apple', 'banana', 'cherry']

# iki listeyi birleştirmek istiyorum
