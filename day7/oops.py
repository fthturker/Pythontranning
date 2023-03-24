# Example1:
# class Myclass:
#     def myfun(self):
#         pass
#     def display(self,name): # self--> sınıfı temsil ediyor
#         print(name)
# #selfi çıkarmamamız lazım ama bu metoda bir argüman yada parametre iletmek istiyorsam
# # o parametreyi ayrı ayrı virgülle belirtmek zorundayım
#
# mc1=Myclass() # object. nesneyi içinde saklamak istiyorsanız bu bir değişkendir ve bu değişken nesneye atıfta bulunmakta
# mc1.myfun()
# mc1.display("jhon") # jhon

# Example2:
# class MyClass:
#     def m1(self):
#         print("This is intance method....")
# # static bir yöntem oluşturduğumuzda, bu yöntemin her nesne için ortak olduğunu
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
#
# mc=MyClass()
# mc.m1()
# mc.m2(100,200) # 100 200
# MyClass.m2(10,20) #10 20 here calling static method directly using class not through object

# Example3:

# class MyClass:
#     a,b=10,20   # class variables (çünkü bu değişkenler sınıfın içinde yaratılmıştır
#                 # bu yüzden bunlar sınıf değişkenleri olarak adlandırılır)
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=MyClass
# mc.add() # 30
# mc.mul() # 200

"""
sınıf değişkenlerine methodun içinden doğrudan erişemeyiz,
bu yüzden bu methodun içindeki bu sınıf değişkenine erişmek için self anahtar sözcüğünü kullanmalıyız
self her zaman sınıfı temsil eder bu yüzden sınıf değişkenlerine erişmek istiyorsam bu yöntemin içinde tanımlamamız gerekir
"""


# Example4:
# i,j=15,25  # global variables
# class MyClass:
#     a,b=10,20   # class variables
#     def add(self,x,y):
#         print(x+y) # x, y are local variables
#         print(self.a+self.b) # a, b are class variables
#         print(i+j) # i, j are global variables
#
# mc=MyClass()
# mc.add(100,200) # 300

# Example5:
# a,b=15,25  # global variables
# class MyClass:
#     a,b=10,20   # class variables
#     def add(self,a,b):
#         print(a+b) # local variables
#         print(self.a+self.b) # class variables
#         print(globals()['a']+globals()['b']) # global variables
# # değişken isimleri aynı ise gobal değişkenlere nasıl ulasabiliriz. bu yüzdenfarklı söz dizimini takip etmeliyiz.
#
# mc=MyClass()
# mc.add(100,200)

# #Example6: once class can have multiple objects
# # bir sınıfın birden çok objesi olabilir
#
# class MyClass:
#     def display(self,name):
#         print("this is display method...")
#         print(name)
# obj1=MyClass()
# obj1.display("Fatih")
#
# obj2=MyClass()
# obj2.display("Yavuz")

# Example7: constructor
# class MyClass:
#     def __int__(self):
#         print("this is constructor")
# # sınıf içinde yapıcı bir yöntem yarattım eğer çağırmak istiyorsanız bu yapıcı bir nesne yaratmamıza gerek yok,
# # sadece bir nesne yaratmamız gerekiyor, ancak nesnenin kendisinin yaratıldığı sırada bu yapıcı onu otomatik olarak çalıştıracaktır.
#
#     def m1(self):
#         print("hello..")
# # ancak bu yöntemi çağırmak istiyorsanız bu yöntemi yalnızca nesne aracılığıyla çağırmamız gerekir.
#
#     def m2(self,x,y):
#         return (x+y)
#
# mc=MyClass() # invoke constructor aıtomatically
# mc.m1() # method we have call explicitely by using object
# print(mc.m2(10,20)) #30

# #Example8:
# class MyClass:
#     name="Fatih"
#     def __init__(self,name): # constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=MyClass("Yavuz") # passing parameter to the constructor

# # Example9:
# # Req: Emp
# # constructor : eid, ename, sal   (çalışan kimliği, çalışan adı ve maaşı)
# # display()    : print eid, ename & sal   (bu yöntem çalışan kimliği, çalışanın adını ve maaşını yazdırmalı)
#
# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid  # class variables  --> yerel değişkenlerimizi sınıf değişkenlerine dönüştürüyoruz
#         self.ename = ename
#         self.sal = sal
#
#     def display(self):
#         print(self.eid, self.ename, self.sal)
#
#
# e1 = Emp(101, 'fatih', 20000)
# e1.display() # 101 fatih 20000
#
# e2 = Emp(102, 'yavuz', 30000)
# e2.display() # 102 yavuz 30000


# Example10:
# Req: Emp
# constructor : eid, ename, sal   (çalışan kimliği, çalışan adı ve maaşı)
# display()    : print eid, ename & sal   (bu yöntem çalışan kimliği, çalışanın adını ve maaşını yazdırmalı)

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid  # class variables  --> yerel değişkenlerimizi sınıf değişkenlerine dönüştürüyoruz
        self.ename = ename
        self.sal = sal

    def __str__(self): # yalnızca dizelerin verilerini yazdıracak
        return (self.ename)

e1 = Emp(101, 'fatih', 20000)
print(e1.ename) # fatih
print(e1) # fatih


















