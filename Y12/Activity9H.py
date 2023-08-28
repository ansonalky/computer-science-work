#DECLARE Mark,Count:INTEGER
#DECLARE Grade:STRING
def GetExamMarks():
    Mark=int(input("Enter your exam mark:"))
    return Mark
def GetGrade(Mark):
    if Mark < 40:
        Grade=("Fail")
    elif Mark < 60:
        Grade=("Pass")
    elif Mark < 80:
        Grade=("Merit")
    else:
        Grade=("Distinction")
    print("Your grade is ", Grade)
Count=int(input("Enter the numbers of marks:"))
for i in range(0,Count):
    Mark=GetExamMarks()
    GetGrade(Mark)