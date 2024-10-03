num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
operator = input("[*,+,/,-] = " )

if operator == "*":
    print (num1*num2)
elif operator == "-":
    print (num1-num2)
elif operator == "/":
    print (num1/num2)
elif operator == "+":
    print (num1+num2)
else:
    print ("error")