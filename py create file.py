a=[]
for j in range(1):
    s=str(input('names '))
    a.append(s)    
print(a)
#file.close()

fie=open('neww.txt','w')
fie.write('aa')
fie.close()

c_file=str(input('enter a file name for txt '))
file=open(c_file,'w')
print('n new file created')

file.write('abc')
file.write('\n')
words=str(input('enter something : '))
file.write(words)
file.write('\n')
file.write('dd')
file.close()
