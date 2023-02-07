'''
    *  
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *  
'''
n=int(input())
for i in range(n):
    for j in range(0,n-1-i):
        print(' ', end='')
    for k in range(0,(i+1)*2-1):
        print('*',end='')
    print()
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(' ', end='')
    for k in range(0,(i)*2-1):
        print('*',end='')
    print()