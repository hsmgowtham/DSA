'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
'''
def isPalindrome(x: int) -> bool:
    if (x<0 or (x!=0 and x%10==0)):
        return False
    rev_n = 0
    while(x>rev_n):
        rev_n = rev_n * 10 + x%10
        x //=10
    return x==rev_n or x==rev_n//10

print(isPalindrome(121))
print(isPalindrome(-323))
print(isPalindrome(120))