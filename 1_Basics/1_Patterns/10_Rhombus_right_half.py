'''
*  
**
***
****
*****
****
***
**
*
'''
n=int(input())
for i in range(n):
    for k in range(0,i+1):
        print('*',end='')
    print()
for i in range(n-1,0,-1):
    for k in range(0,i):
        print('*',end='')
    print()