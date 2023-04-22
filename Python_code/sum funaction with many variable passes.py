def sum(a, b, *more):
    ans = a + b
    for i in more:
        ans += i
    return ans


ans = sum(1, 2, 3, 4, 5, 6)
print(ans)
