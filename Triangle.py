print("Please insert the first number") 
a = int(input())
print("Please insert the second number")
b = int(input())
print("Please insert the Third number")
c = int(input())

if a<b+c and b<a+c and c<a+b :
    print("Yes, you can make a triangle")

else : 
     print("No, you cant make a triangle")
