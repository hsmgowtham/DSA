'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

n=int(input())
for i in range(n,0,-1):
    for j in range(0,i):
        print('*', end=' ')
    for j in range(0,(n*2)-(i*2)):
        print(' ', end=' ')
    for j in range(0,i):
        print('*', end=' ')
    print()
for i in range(n):
    for j in range(0,i+1):
        print('*', end=' ')
    for j in range(0,(n*2)-((i+1)*2)):
        print(' ', end=' ')
    for j in range(0,i+1):
        print('*', end=' ')
    print()