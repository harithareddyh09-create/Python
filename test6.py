print("----CALCULATOR----")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
operator=(input("enter an operator (=,-,/,%,*) to perform the operation:"))
if operator=="+":
    print("sum of digits:",a+b)
elif operator=="-":
    print("subraction of digits:",a-b)
elif operator=="/":
    if b==0:
        print("division is not possible with zero")
    else:
        print("division of digits:",a/b)
elif operator=="%":
    if b==0:
        print("modulus is not possible with zero")
    else:
        print("modulus of digits:",a%b)
elif operator=="*":
    print("multiplication of digits:",a*b)
else:
    print("Invalid operator")