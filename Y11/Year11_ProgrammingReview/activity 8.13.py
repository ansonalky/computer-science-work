#8.11
rows=3
cols=5
students=3
result=[0,0,0,0,0]
students=["           " for h in range(students)]
subject=[["           "for t in range(cols)]for o in range(rows)]
highest_list=[[0 for t in range(cols)]for o in range(rows)]
lowest_list=[[0 for t in range(cols)]for o in range(rows)]
average=[[0 for t in range(cols)]for o in range(rows)]
largest=0
lowest=0
total=0
for a in range(0,3):
    students[a]=input("Enter students name:")
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
        average[a][n]=total/5
        highest_list[a][n]=result[largest]
        lowest_list[a][n]=result[lowest]
for i in range(0,3):
    print("For",students,",")
    for j in range(0,5):
        print("the highest score is",highest_list[i][j])
        print("the lowerst score is",lowest_list[i][j])
        print("the average score is",average[i][j])