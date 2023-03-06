# Control statements
# normal olarak programınızı yazdığınızda program adım adım doğru şekilde yürütülür
"""
3 tane kontrol ifadeleri vardır
1-) conditional statements
    if      if..else    elif
2-) looping statements
    while   for
3-) jumping statements
    break   continue
"""

# 1-) conditional statements
#    if      if..else    elif

# Example 1: Print a person is eligible for vote or not
# age>=18

# age = 15
# if age >= 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

# python'da girinti çok önemlidir bu nedenle, if koşulu kullanıldığında yalnızca bir sekme alanı vermemiz gerektiğinde,
# bir sekme alanı gereklidir

#Example 2

# if True:
#     print("true condition")
# else:
#     print("false condition")

#Example 3

# if 1:
#     print("one")
# else:
#     print("not one")

#Example 4  : Find a number is even/add   num%2=0
num=10

if num%2==0:
    print("Given number is even")
else:
    print("Given is number add")

