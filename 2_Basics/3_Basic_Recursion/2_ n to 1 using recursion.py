def printnums(n):
    if n==0:
        return
    print(n)
    printnums(n-1)
    
printnums(5)