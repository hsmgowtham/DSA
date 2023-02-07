def printnums(n):
    if n==0:
        return
    printnums(n-1)
    print(n)
printnums(5)