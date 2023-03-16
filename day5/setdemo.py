"""
set
A set is a collection which is unordered and unindexed. In python sets are written with curly brackets.
bir küme, sıralanmamış ve indekslenmemiş bir koleksiyondur
"""
#Example1: creating set
# myset={"appple","banana","cherry"}
# print(myset) # {'banana', 'appple', 'cherry'}
"""
çıktıya baktığımızda, verilerin tam olarak aynı sırada yazdırılmadığını göreblirsiniz
set unordered bir listedir, undordered: o değerleri sırasıyla saklamışsak aynı sırayla görüntülemiyor
"""

#Example2: Accessing items from set
# myset={"appple","banana","cherry"}
# for i in myset:
#     print(i)

#Example3: value exists in set or not
#öğenin kümede var olup olmadığını kontrol etmek istediğimi varsayalım,
#bunun için, değerin kümede var olup olmadığını kontrol etmek için tekrar operatörde kullanabiliriz
# myset={"appple","banana","cherry"}
# print("banana" in myset) #True
# print("banana2" in myset) #False

#Example4: addding items to set
#sete yeni bir ürün eklemek istiyorum
#1. yöntem add()    ---> kullanarak bir seferde yalnızca tek bir öğe ekleyebiliriz
#2. yöntem update() ---> kullanarakbir seferde birden fazla öğe ekleyebiliriz.
# myset={"appple","banana","cherry"}
# #myset.add("orange")
# myset.update(["mongo","grapes"])
# print(myset)        # {'appple', 'orange', 'cherry', 'banana'}
#                     # {'cherry', 'grapes', 'banana', 'mongo', 'appple'}

#Example5: find number of items in a set
#bir kümedeki öğe sayısını bulun  ---> len()
# myset={"appple","banana","cherry"}
# print(len(myset)) #3

#Example6: remove item from set ----> remove()    ----> discard() atama işlemi
#varsayalım öğeyi kaldırmak istiyorum bu mümkün mü değil mi çünkü set değişkendir set değişmez
# set is mutable. işlemin mümkün olduğu anlamına gelir yani
# yeni değerler ekleyebiliriz,çıkarabiliriz,değiştirebiliriz,kaldırabiliriz

# myset={"appple","banana","cherry"}
# myset.remove("banana")
# print(myset) # {'cherry', 'appple'}
#myset.remove("xyz") # KeyError: 'xyz'

# myset.discard("banana")
# print(myset) # {'appple', 'cherry'}
# myset.discard("xyz") # will not throw any error

# remove ile discard arasındaki fark
# kaldır işlevini kullandığımda olmayan bir öğe yazdığım da hata veriyor ama atamada hata olarak vermiyor

#Example7: clear all items from set
#seti temizlemek istiorum setteki tüm öğeleri temizlemek istiyorum
# myset={"appple","banana","cherry"}
# myset.clear()
# print(myset) # set()
#
# #set değişkenini tamamen silmek istiyorum bunun için del() kullanılır
# del myset
# print(myset) # NameError: name 'myset' is not defined
# # clear fonksiyonu sadece set değişkenini verilerle birlikte tamamen silecek olan del anahtar kelimesi setten değerleri temizler

#Example8: joining 2 sets --> iki set nasıl birleştirilir --> union() kulanılır
# set1={"a","b","c"}
# set2={1,2,3}
# set3=set1.union(set2)
# print(set3) # {1, 2, 3, 'c', 'b', 'a'}

# güncelleme işlevini kullanarak iki kümeyi birleştirmenin bir yolu daha var update()
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1) # {1, 2, 3, 'c', 'a', 'b'}



