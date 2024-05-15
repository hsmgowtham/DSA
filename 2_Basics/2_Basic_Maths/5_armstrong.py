'''
153 = 1^3 + 5^3 + 3^3
'''
n=int(input())
x=n
sum=0
while x!=0:
    sum+=(x%10)**3
    x//=10
if sum==n:
    print("yay it's armstrong num")
else:
    print("It's Not a armstrong num")
    