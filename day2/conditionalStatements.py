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
# num=10
#
# if num%2==0:
#     print("Given number is even")
# else:
#     print("Given is number add")

# Example 5 : if else in single line (ternary operator)
# num=10
# print('Even number') if num%2==0 else print ('odd number')

# Example 6 : if else - Multiple statements in Single Line
# çoklu print deyimlerini {} parantezler içinde olur ve ardındam koşulu sürdürmek if else

# a=20
# {print('hello'),print('python')} if a>=10 else {print('hi'),print('java')}

# Example 7 : Multiple conditions using elif

weekno = 7

if weekno == 1:
    print('sunday')
elif weekno == 2:
    print('monday')
elif weekno == 3:
    print('tuesday')
elif weekno == 4:
    print('wednesday')
elif weekno == 5:
    print('thurday')
elif weekno == 6:
    print('friday')
elif weekno == 7:
    print('saturday')
else:
    print('Invalid week number')

"""
Assigments
----------------
1) Check the given number is Positive or negative
2) Check the largest of 2 numbers
3) Check the largest of 3 numbers
4) Print week number if you provide weekname as input
"""