file=open('no.txt','w')
limit=int(input('enter loop limit :'))
for j in range (limit):
    print(j)
    file.write('write something \n')
file.close()
print('file closed')


file=open('no.txt','a')
b=[]
for j in range(10):
    name=str(input('enter name : '))
    b.append(j)

file.write(b)
    
file.close()