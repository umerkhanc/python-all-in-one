numbers=[33,5,78,65,73,223,55,44,332,223,1,234,54,908]
od_n=[]
ev_n=[]


for num in numbers:
    od_n.append(num) if (num % 2) else ev_n.append(num)
print('numbers:      {}'.format(numbers))
print('odd numbers:      {}'.format(od_n))
print('even numbers:      {}'.format(ev_n))