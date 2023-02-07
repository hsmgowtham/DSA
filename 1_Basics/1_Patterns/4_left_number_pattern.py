'''
1
22
333
4444
55555
'''

n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(i+1, end=' ')
    print()