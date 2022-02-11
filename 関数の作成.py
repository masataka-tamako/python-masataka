def mysum(numberlist):
    sum_val = 0
    for x in numberlist:
        sum_val = sum_val + x
    return sum_val

l = [1,2,3,4,5,6,7,8,9,10]
ans = mysum(l)
print(ans)