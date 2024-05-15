'''
12345
len = 5
'''
n=int(input())
x=n
c=0
while x!=0:
    x//=10
    c+=1
print(f'{c=}')