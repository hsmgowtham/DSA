'''
*********
 *******
  *****
   ***
    *  
'''
n=int(input())
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(' ', end='')
    for k in range(0,(i)*2-1):
        print('*',end='')
    print()