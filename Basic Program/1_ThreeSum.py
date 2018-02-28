def threesum(a,b,c):
    sum = a+b+c

    if a == b == c:
        sum = sum*3
    return sum

print(threesum(2,3,4))

print(threesum(10,10,10))
