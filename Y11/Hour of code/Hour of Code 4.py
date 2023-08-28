# hour of code #4
temp=int(input("Enter temperature:"))
if temp<=0:
    print("Water is freezing")
elif temp>=100:
    print("Water is boiling")
else:
    print("Water is in liquid form")