#DECLARE Password,Password2,Attempt : STRING
#DECLARE Count : INTEGER
def GettingPassword():
    Password=input("Enter your password:")
    Password2=input("Enter your password:")
    while Password2 != Password:
        Password2=input("Re-enter your password:")
    return Password

def AttemptingPassword(Count,Password):
    print("You have 3 times to enter the correct password")
    Attempt=""
    while Count<3 and Attempt != Password:
        Attempt=input("Enter your password:")
        Count+=1
    if Attempt!=Password:
        print("Password is incorrect")
    else:
        print("Password is correct")

Count=1
Password=GettingPassword()
AttemptingPassword(Count,Password)

