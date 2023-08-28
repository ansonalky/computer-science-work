# hour of code #18
str=input("Enter String:")
str=str.replace(" ","")
if len(str) == 0:
    print('')
if len(str) % 2 == 0:
    print(str[(len(str) - 1) // 2])
    print(str[(len(str)//2)])
else:
    print(str[len(str) // 2])