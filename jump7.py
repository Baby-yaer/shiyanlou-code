n range(101):
    m = n%10
    p = n//10
    if n%7==0 or m == 7 or p == 7:
         continue
    print('{}\n'.format(n))
