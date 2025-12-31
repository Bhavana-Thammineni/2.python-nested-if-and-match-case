"""rating = float(input("enter the values :"))
if rating <0 or rating >5:
    print("pls enter the valid rating")
elif rating<= 5 and rating >= 4.5:
    print("movie is blockbooster")
elif rating >4:
    print("movie is superhit")
elif rating >3.5:
    print("movie is hit")
elif rating >3:
    print("movie is good")
elif rating >2.5:
    print("movie is average")
else:
    print("movie is flop");"""

#Write a Python program using nested if to find the largest of three numbers
"""num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))
num3 = int(input("enter the number: "))
if num1>num2:
    if num1>num3:
        print("greater number is",num1)
    else:
        print("greater number is",num3)
else:
    if num2>num3:
        print("greater number is",num2)
    else:
        print("greater number is",num3)"""

#Write a program to check whether a number is:PositiveNegativeZero using nested if statements. 
"""number= float(input("enter the number :"))
if number>=0:
    if number>0:
        print("number is POSITIVE",number)
    else:
        print("number is zero")
else:
    print("nUMBER IS negative")"""

#Write a Python program using nested if to check whether a student is: pass fail distinction
"""marks =int(input("enter the marks obtianed"))
if marks>35:
    if marks>60:
        print("distinction")
    else:
        print("pass")
else:
    print("failed")"""

#Write a program using nested if to check whether a year is a leap year.
"""year =int(input("enter the year :"))
if year%4 ==0:
    if year% 100 ==0:
        if year%400 ==0:
            print("leap ysear")
        else:
            print("not leap year")  
    else:
        print("leap year")
else:
    print("not leap year")"""

#Write a program using nested if to determine whether a person is: Child Teenager Adult Senior citizen
"""age = int(input("enter the age :"))
if age >=0:
    if age<13:
      print("child")
    else:
       if age<19:
         print("teenager")
       else:
              if age<55:
                  print("adult")
              else:
                  print("senior citizen")                   
else:
   print("invaild")    """

#Write a Python program using match-case to display the day of the week based on a number (1–7)
"""num =int(input("enter the value: ")) 
match num:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thurday")
    case 5:
        print("frifday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("no vaild day num")"""

#Write a Python program to store a student’s name, age, and percentage in variables and display them.
"""student_name = input("enter the name :")
age = int(input("enter the age :"))
percentage = float(input("enter the percentage: "))
print("student name ", student_name)
print("age",age)
print("percentage",percentage)"""

#Write a program to take two numbers as input and display their sum, difference, product, and quotient.
# Program to perform arithmetic operations on two numbers

"""number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operation = input("Enter the operation (sum, difference, product, quotient): ")

if operation == "sum":
    print("Sum =", number1 + number2)

elif operation == "difference":
    print("Difference =", number1 - number2)

elif operation == "product":
    print("Product =", number1 * number2)

elif operation == "quotient":
    if number2 != 0:
        print("Quotient =", number1 / number2)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid operation")"""

 #Write a program to check and display the data type of user input.
"""num1 = input("Enter the value: ")
print(type(num1))
num2 = float(input("Enter the value: "))
print(type(num2))
num3 = int(input("Enter the value: "))
print(type(num3))
#OR
value = input("Enter text or number: ")
if value.isdigit():
    print("Data type is int")
elif "." in value:
    print("Data type is float")
else:
    print("Data type is string")"""

#typecasting int to float and float to int
"""a = int(input("enter integer: "))
print(float(a))
b = float(input("enter the float value :"))
print(int(b))"""

#Write a program to swap two numbers using a temporary variable
"""a = int(input("enter the 1 value: "))
b = int(input("enter the 1 value: "))
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)"""

#Write a Python program to demonstrate:
# Program to demonstrate arithmetic, relational, and logical operators

"""a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Arithmetic operators
print("Arithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
# Relational operators
print("\nRelational Operations:")
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
# Logical operators
print("\nLogical Operations:")
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))"""

#Write a program to check whether a number is even or odd using operators.
"""num = int(input("enter the value"))
if num%2 ==0:
    print("even")
else:
    print("odd")"""

#Write a program to check whether a number is divisible by 5 and 11.
"""num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print(num, "is divisible by both 5 and 11")
else:
    print(num, "is not divisible by both 5 and 11")"""

#Write a program to check whether a number is positive.
"""num = int(input("enter the value"))
if num >0:
    print("postive")
elif num<0:
    print("negative")
else:
    print("zero")"""

#Write a program to check whether a person is eligible to vote
"""num = int(input("enter the age :"))
if num>=18:
    print("can vote")
else:
    print("no vote eliglible")"""

#Write a program to check whether a number is a multiple of 3
a = int(input("enter the value"))
n =1
if n<10:
    print("mutliple",a*n)
    n=n+1
else:
    print("invaild cnse")