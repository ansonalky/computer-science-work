#8.10
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
if num1!=num2:
    print("They are not equal")
    if num1>num2:
        print("Number 1 is larger and number 2 is smaller")
    else:
        print("Number 2 is larger and number 1 is smaller")
else:
    print("They are equal")
num3=int(input("Enter number:"))
if num1!=num2 and num1!=num3:
    print("they are not equal")
    if num1>num2:
        if num1>num3:
            print("Number 1 is the largest")
        else:
            print("Number 3 is the largest")
    elif num2>num3:
        print("Number 2 is the largest")
    else:
        print("Number 3 is the largest")

    if num1<num2:
        if num1<num3:
            print("Number 1 is the smallest")
        else:
            print("Number 3 is the smallest")
    elif num2<num3:
        print("Number 2 is the smallest")
    else:
        print("Number 3 is the smallest")
else:
    print("They are equal")