'''
    *  
   ***
  *****
 *******
*********
'''
n=int(input())
for i in range(n):
    for j in range(0,n-1-i):
        print(' ', end='')
    for k in range(0,(i+1)*2-1):
        print('*',end='')
    print()