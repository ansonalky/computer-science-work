#8.11
result=[0,0,0,0,0]
subject=["             ","                    ","                      ","                      ","                ","             "]
highest_list=[" "," "," "," "," "," "]
lowest_list=[" "," "," "," "," "," "]
average=[0,0,0,0,0,0]
largest=0
lowest=0
total=0
for n in range(0,6):
    subject=input("Enter subject name:")
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
    average[n]=total/5
    highest_list[n]=result[largest]
    lowest_list[n]=result[lowest]
for j in range(0,5):
    print("the highest score is",highest_list[j])
    print("the lowerst score is",lowest_list[j])
    print("the average score is",average[j])