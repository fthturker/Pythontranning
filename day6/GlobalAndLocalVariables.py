#Example1:
# global_var=20  #global variable
# def func():
#     local_var=10 #local variable
#     print(local_var) # local variable'a fonksiyonun içinden ulaşabiliriz
#     print(global_var) #global variable'a fonksiyonun içindeki fonksiyonun dışında her yere erişebiliriz
# func()
#
# #print(local_var) # yerel olduğundan fonksiyonun dışında yazdıramıyoruz hata veriyor
# print(global_var) # global olduğundan fonksiyonun dışında da yazdırabiliyoruz

# #Example2:
# xy=100 # global variable
# def cool():
#     xy=200 # değişken ismi aynı ama local variable
#     print(xy)
# cool() #200
# print(xy) #100

#Example3: Using global variable in local variable and update value
# global değişkeni local değişkenin içinde kullanarak update ettik.
xy=100 # global variable
def cool():
    global xy
    xy=200 # global variable
    print(xy)
cool() #200
print(xy) #200

#Example4:
