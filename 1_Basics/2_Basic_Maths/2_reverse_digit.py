'''
Given a signed 32-bit integer x,
return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0
'''
def reverse(x: int) -> int:
    is_negative = False
    if x<0:
        is_negative = True
    n=0
    x=abs(x)
    while x!=0:
        n=n*10 + (x%10)
        x//=10
    n=-n if is_negative else n
    if n>2**31 or n<-2**31:
        return 0
    return n
print(reverse(123))
print(reverse(-324))
print(reverse(120))