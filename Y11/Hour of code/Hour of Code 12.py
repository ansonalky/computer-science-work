# hour of code #12
num=int(input("Enter number(1-5):"))
while num<1 or num>5:
    print("It is not valid. Please enter a number between 1 and 5.")
    num=int(input("Enter number(1-5):"))
print("It is finally valid.")