"""
dictionary'de verileri anahtar ve değer şeklinde depolayacağız (key,value)
A dictionary is a collection which is unordered, changeable(mutable) and indexed.
In python dictionaries are written with curly brackets --> {} , and they have keys and values.
dictionary--> değiştirilebilir bir nesnedir
              sırasızdır
key     = value
product1=100  key benzersiz olmalı
product2=200
product=500
"""
#Exampe1: creating dictionary
# mydic={101:"x",102:"y",103:"z"}
# print(mydic) # {101: 'x', 102: 'y', 103: 'z'}

#Example2: Access items from dictionary
# sözlükten öğelere erişmek
# indeks kavramı yok ama key indeks olarak çalışıyor
# mydic={
#     "brand":"hnydai",
#     "model":"i10",
#     "year":2021
# }
# print(mydic["brand"]) # hnydai
# print(mydic["model"]) # i10
# print(mydic["year"]) # 2021
#
# #using get() fonksiyonunu kullanarak da dictionary deki öğelere ulaşabiliriz
# x=mydic.get("brand")
# print(x) # hnydai
# # print(mydic.get("brand")) # hnydai

#Example3:change values in dictionary
# sözlükteki değerleri değiştirmek istiuorum
# mydic={
#     "brand":"hnydai",
#     "model":"i10",
#     "year":2021
# }
# print(mydic) #{'brand': 'hnydai', 'model': 'i10', 'year': 2021}
# mydic["year"]=2022
# print(mydic) #{'brand': 'hnydai', 'model': 'i10', 'year': 2022}

#Example4: reading items from dictionary using loop
# mydic={
#     "brand":"hnydai",
#     "model":"i10",
#     "year":2021
# }
# for i in mydic:
#     print(i) # 3 prints only keys from dictionary
# # sadece key'leri yakaladık,ve sadece onları yazdırdık
#
# # yalnızca value ları yazdırmak istiyorum, bunu nasıl yapabiliriz?
# # key'i bilirsem value 'da çıkarabiliriz
# for i in mydic:
#     print(mydic[i]) # prints only values from dictionary

# for i in mydic.values():
#     print(i)  # prints only values from dictionary

# for x,y in mydic.items():
#     print(x,y) # print keys alaong with the value (çıktı anahtarlarını deperle birlikte)

#Example5: check key is exist in dictionary or not
#anahtarın sözlükte olup olmadığını
# mydic={
#     "brand":"hnydai",
#     "model":"i10",
#     "year":2021
# }
# if "model" in mydic:
#     print("exixts") # true
# else:
#     print("not exists")
#
# print("model" in mydic) #True

#Example6: find number of items in dictionary
#sözlüğümde toplam kaç tane öğe olduğunu bulmak istiyorum
# mydic={
#      "brand":"hnydai",
#      "model":"i10",
#      "year":2021
# }
# print(len(mydic)) # 3

#Example7: Adding items to dictionary -- sözlüğe öğeler ekleme
# mydic={
#      "brand":"hnydai",
#      "model":"i10",
#      "year":2021
# }
# mydic["color"]="red"
# print(mydic) # {'brand': 'hnydai', 'model': 'i10', 'year': 2021, 'color': 'red' }
#aynı anda birden çok öğe ekleyemeyiz bu nedenle birden çok ifade yazmak zorunddayız

#Example8: remove item from dicitonary
# mydic={
#      "brand":"hnydai",
#      "model":"i10",
#      "year":2021
# }
# mydic.pop("year")
# print(mydic) # {'brand': 'hnydai', 'model': 'i10'}

# del mydic["year"]
# print(mydic) # {'brand': 'hnydai', 'model': 'i10'}

#tüm sözlüğü silmek istiyorum
# del mydic
# print(mydic) # NameError: name 'mydic' is not defined
#
# mydic.clear()
# print(mydic) # {}

#Example9: copying dictionary
mydic1={
     "brand":"hnydai",
     "model":"i10",
     "year":2021
}
#using copy()
# mydic2=mydic1.copy()
# print(mydic2) # {'brand': 'hnydai', 'model': 'i10', 'year': 2021}

# without using copy()
# mydic2=mydic1
# print(mydic2) # {'brand': 'hnydai', 'model': 'i10', 'year': 2021}

