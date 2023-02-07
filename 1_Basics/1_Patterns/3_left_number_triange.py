'''
1
12
123
1234
12345
'''

n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1, end=' ')
    print()