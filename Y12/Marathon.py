#DECLARE Hours, Minutes, Seconds: INTEGER
#DECLARE TotalTime, PBSeconds: INTEGER

print("We are asking for time you took to run the marathon") #Entering marathon time in H/M/S
Hours=int(input("Enter hours:"))
Minutes=int(input("Enter minutes:"))
Seconds=int(input("Enter seconds:"))

TotalTime=(Hours*60*60)+(Minutes*60)+Seconds #Convert time to seconds

PBSeconds=int(input("Enter your PB:"))#Get PB in seconds

if TotalTime<PBSeconds:#Compare PB with marathon time
    PBSeconds=TotalTime

print("PB is now:", PBSeconds)#OutputPB