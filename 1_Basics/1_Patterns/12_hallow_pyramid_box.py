'''
1      1
12    21
123  321
12344321
'''

n=int(input())
for i in range(n):
    for j in range(0,i+1):
        print(j+1, end='')
    for k in range(n*2-(i+1)*2):
        print(' ',end='')
    for p in range(i+1,0,-1):
        print(p, end='')
    print()