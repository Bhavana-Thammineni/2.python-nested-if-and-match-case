# 2.python-nested-if-and-match-case
programs on match case and nested if
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
