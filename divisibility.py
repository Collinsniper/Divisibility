# Python Program to Check Number is Divisible by 2 and 5

number = int(input(" Please Enter any Positive Integer : "))

if((number % 2 == 0) and (number % 5 == 0)):
    print("Given Number {0} is Divisible by 2 and 5".format(number))
else:
    print("Given Number {0} is Not Divisible by 2 and 5".format(number))