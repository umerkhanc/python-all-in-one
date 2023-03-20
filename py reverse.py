s=input("enter a word ")
def pa(string):
    x=""
    for i in string:
        x =i+x
    return x

print(pa(s))