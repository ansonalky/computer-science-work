#DECLARE Numbers, Value, Total, Average : INTEGER
def finding_average(Numbers): 
    Total=0
    for i in range(0,Numbers):
        Value=int(input("Enter the a value:"))
        Total=Total+Value
    Average=Total/Numbers
    print ("The average is", Average)
Numbers=int(input("Enter the number of values:"))
finding_average(Numbers)