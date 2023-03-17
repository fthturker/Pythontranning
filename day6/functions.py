#Example1:
# def myfun():
#     print("hello")
# myfun() # call the function

#Example2:
# def myfun(name):
#     print("Hello",name)
# myfun("Smith") #Hello Smith

#Example3:
# def cal(a,b):
#     return (a+b)
#
# sum=cal(100,200)
# print(sum) # 300
# print(cal(10,20)) #30

#Example4:
# def func():
# #     return
# def func():
#     i=10
#
# print(func()) # None

#Example5:
# def cal(a,b):
#     print(a+b) # hiçbir şey döndürmeyecek çünkü sadece buraya yazdırıyor
# cal(10,20) # 30

def cal(a,b):
    return(a+b) #çıktı al yerine baskıya geri dön diyorum
print(cal(10,20)) # 30