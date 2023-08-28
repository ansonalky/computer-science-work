# hour of code #27
f = open("Text.txt", mode='r', encoding='utf-8')
f2 = open("Text2.txt", mode='w+', encoding='utf-8')
copy=(f.read())
with open("text2.txt",'w',encoding = 'utf-8') as f2:
   f2.write(copy)
f.close()
f2.close()
print("Done")