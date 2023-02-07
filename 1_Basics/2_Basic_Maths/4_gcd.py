'''
GCD of two numbers
Greatest Common Divisor
GCD of 3 and 6 is 3
'''
a=3
b=6
ans=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        ans=i
print(ans)
