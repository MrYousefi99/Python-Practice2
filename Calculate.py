import math


def sum() :
    print("Please insert the first number")
    a = int(input())
    print("Please insert the second number")
    b = int(input())
    sum = a+b

    print("Sum is " , sum)

def sub() :
        print("Please insert the first number")
        a = int(input())
        print("Please insert the second number")
        b = int(input())
        sub = a-b

        print("Submission is " , sub)


def mul() :
        print("Please insert the first number")
        a = int(input())
        print("Please insert the second number")
        b = int(input())
        mul = a*b

        print("Multiplication is " , mul)


def div() : 
    
        print("Please insert the first number")
        a = int(input())
        print("Please insert the second number")
        b = int(input())
        div = a/b

        print("Division is " , div)


def pow() : 
        print("Please insert the number")
        a = int(input())
        print("Please insert the Power")
        b = int(input())
        pow = math.pow(a, b)

        print("Result is " , pow)


def sin() : 
        print("Please insert the Degree")
        a = int(input())
        Sin = math.sin(math.radians(a))
        print("sinus is " , Sin)


def cos() :
        print("Please insert the Degree")
        a = int(input())
        Cos = math.cos(math.radians(a))
        print("cosine is " , Cos)

def tan() : 
        print("Please insert the Degree")
        a = int(input())
        Tan = math.tan(math.radians(a))
        print("Tangent is " , Tan)

def cot() : 
        print("Please insert the Degree")
        a = int(input())
        Cot = math.cos(math.radians(a))/math.sin(math.radians(a))
        print("cotangent is " , Cot)        






while(True) :
    
   print("Welcome To The Calculator")

   print("1-Sum")

   print("2-Submission")

   print("3-Multiplication")

   print("4-Division")

   print("5-Power")

   print("6-sinus")

   print("7-cosine")

   print("8-Tangent")

   print("9-cotangent")

   print("Please enter your desired option")

   inp = int(input())

   if inp == 1 :  sum()
   elif inp == 2 :  sub()
   elif inp == 3 :  mul()
   elif inp == 4 :  div()
   elif inp == 5 :  pow()
   elif inp == 6 :  sin()
   elif inp == 7 :  cos()
   elif inp == 8 :  tan()
   elif inp == 9 :  cot()

   print("Thank you for your attention/n")

