# hour of code #5
num=int(input("Enter number(1-12):"))
month=("January","Feburary","March","April","May","June","July","August","September","October","November","December")
if num>=1 and num<=12:
    print(month[num-1])
else:
    print("the number is not valid")