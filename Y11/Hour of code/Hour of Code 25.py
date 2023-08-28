# hour of code #25
Numberlist = [[0 for i in range(5)] for j in range(5)]
for n in range(0,5):
    for a in range(0,5):
        Numberlist[a][n]=0
row=int(input("Enter numbers:"))
col=int(input("Enter numbers:"))
while row!=0 or col!=0:
    Numberlist[row-1][col-1]=Numberlist[row-1][col-1]+1
    row=int(input("Enter numbers:"))
    col=int(input("Enter numbers:"))
print(Numberlist)