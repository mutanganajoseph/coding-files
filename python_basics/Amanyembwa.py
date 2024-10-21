def a_n(n):
    if n == 1:
        return 1
    else:
        return 1 + a_n(n-1)

print(a_n(2008))
