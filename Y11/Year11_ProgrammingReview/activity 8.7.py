#8.7
total=0
count=0
weight=int(input("Enter weight:"))
number=int(input("Enter number of sacks:"))
while weight>0 or number>0:
    total=(weight*number)+total
    count=count+number
    weight=int(input("Enter weight:"))
    number=int(input("Enter number of sacks:"))
print("The total weight is",total,"kg.")
print("The total number is",count,".")
