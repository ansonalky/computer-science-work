ZOO = [['' for k in range(3)] for l in range(8)] #initial array

def readfile():
    index=0
    f=open("AnimalsUnsorted.txt","r+") #open file
    FileString=f.readline().strip() #read the first line
    while FileString != "":
        ZOO[index][0] = FileString        #repeat this three times
        FileString=f.readline().strip()
        ZOO[index][1] = int(FileString)
        FileString=f.readline().strip()
        ZOO[index][2] = FileString
        FileString=f.readline().strip()
        index+=1
    f.close() #close file



def GetInfo():
    min=101
    max=-1
    total=0
    average=0
    Europe=0

    
    for i in range (8):
        if ZOO[i][1] < min: #get min age
            min=i

        if ZOO[i][1] > max: #get max age
            max=i

        total=total+ZOO[i][1]     #get total

        if ZOO[i][2] == "Europe":    #check regions
            Europe+=1

    average=total/8             #get average
    
    print("The age of the youngest animal   :",ZOO[min][0])
    print("The age of the oldest animal     :",ZOO[max][0])
    print("The total age of the animals     :",total)
    print("The average age of the animals   :",average)
    print("The number of animals from Europe:",Europe)


def search():
    index=-1
    search=input("Which animal do you want to find?")
    for i in range (8):
        if str(search.upper()) == str(ZOO[i][0].upper()):
            index=i+1
    if index>0:
        print("The array index is: ",index)
    else:
        print("The array index is: -1")

def BubbleSort():
    MaxIndex=8
    Swaps=True
    n= MaxIndex-1
    Passes=0
    while Swaps==True and Passes < MaxIndex-1:
        Swaps=False
        for j in range(0,n):
            if ZOO[j][0] > ZOO[j+1][0]:
                Temp=ZOO[j][0]
                ZOO[j][0]=ZOO[j+1][0]
                ZOO[j+1][0]=Temp
                Temp=ZOO[j][1]
                ZOO[j][1]=ZOO[j+1][1]
                ZOO[j+1][1]=Temp
                Temp=ZOO[j][2]
                ZOO[j][2]=ZOO[j+1][2]
                ZOO[j+1][2]=Temp
                Swaps=True
        n -=1
        Passes +=1
    print(ZOO)



def WriteFile():
    f = open("AnimalsSorted.txt", "x")  #create file
    f.close
    file = open("AnimalsSorted.txt", "w") #open file
    for i in range(8):
        for j in range(3):
            file.write(str(ZOO[i][j])+"\n") #write items into file
    file.close

#main program
readfile()
GetInfo()
search()
BubbleSort()
WriteFile()