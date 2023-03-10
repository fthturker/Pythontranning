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
mylist=["apple","banana","cherry"]
# apple 'ın bu listede olup olmadığını kontrol etmek istiyorum
if "apple" in mylist:
    print("yes, apple is present") # yes, apple is present
else:
    print("no, apple is not present")
