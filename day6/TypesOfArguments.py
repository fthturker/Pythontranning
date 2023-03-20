# #Example1:
# def func(i,j):
#     print(i,j)
# #func(10,20) # 10 20 # positional arguments
# # konumsal argümanlar olarak adlandırılır, çünkü pozisyona bağlı olarak veriler atayacaktır
# # bu nedenle ilk konumm değeri ilk değişken ikinci değişkende ikinvi konum değeri atanmıştır
#
# func(j=20,i=10) # 10 20 # keyword arguments
# # burada hangi değişkene hangi değerin atanması gerektiğini söylüyorum
# #anahtar kelime argümanlarının konumu önemli değil

# #Example2: default values assigned to positional arguments
# def func(i,j=10):
#     print(i,j)
# func(100,200) # 100 200
# func(100) # 100 10

#Example3:keyword arguments
# def greetings(name,greetmsg):
#     print(greetmsg+"    "+name)
#
# greetings(name="Fatih", greetmsg="Hello") # Hello    Fatih
# greetings(greetmsg="Hello", name="Fatih") # Hello    Fatih

#Example4:
# def my_func(a,b,c):
#     print(a,b,c)
#
# my_func(10,20,30) # positional arguments
# my_func(a=10,b=20,c=30) # Keyword arguments
# my_func(b=20,a=10,c=30) # Keyword arguments
#
# my_func(10,20,c=30) # 10 20 30 # konumsal ve anahtar kelime argümanlarının kombinasyonu
# my_func(10,b=20,c=30) # 10 20 30
#my_func(10,b=20,30) #this is wrong as positional argument must appear any keyword argument
# bu yanlış bir ifadedirçünkü konumsal argüman herhangi bir anahtar kelime argümanından
# önce görünmelidir. bu çalışorken hatırlamanız gereken basit bir kuraldır
#my_func(10,30,b=20)

#Example5:
def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(largest(100,200)) # (200,100)
print(largest(20,10)) # (20,10)

#bunları bir değişkende saklamak istiyorum
res=largest(10,20)
print(res) # (20, 10)