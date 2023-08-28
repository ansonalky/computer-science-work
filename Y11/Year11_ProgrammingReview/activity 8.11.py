#8.11
result=[0,0,0,0,0]
largest=0
lowest=0
total=0
for i in range(0,5):
    result[i]=int(input("Enter test result:"))
    total=result[i]+total

if result[0]>result[1]:
    largest=0
else:
    largest=1

if result[0]<result[1]:
    lowest=0
else:
    largest=1
    
for i in range(2,5):
    if result[largest]>result[i]:
        largest=largest
    else:
        largest=i
    
    if result[lowest]<result[i]:
        lowest=lowest
    else:
        lowest=i
average=total/5
print("The largest one is",result[largest])
print("The lowest one is",result[lowest])
print("The average is",average)