#8.6
def count():
    a=0
    for i in range(0,10):
        a=a+3
        print(a)

def condition():
    a=0
    i=0
    while i<10:
        a=a+3
        print(a)
        i+=1

function=int(input("Enter 1 or 2:"))
if function == 1:
    count()
elif function ==2:
    condition()
else:
    print("no function found")