
def maximum(a, b):
    if a > b:
        return a
    return b


# get no. of items (n) and bag capacity (c)
n, c = (int(x) for x in input().split())

# allocate static matrices for weights and values
weights = [0 for x in range(n)]
values = [0 for x in range(n)]
# fill matrices with inputs
for x in range(n):
    weights[x], values[x] = (int(y) for y in input().split())

t = [[0 for x in range(c + 1)] for y in range(n + 1)]
i = 1
j = 0
while 1:
    if j >= weights[i - 1]:
        t[i][j] = maximum(t[i - 1][j], t[i - 1][j - weights[i - 1]] + values[i - 1])
    else:
        t[i][j] = t[i - 1][j]
    j += 1
    if j > c:
        j = 0
        i += 1
        if i > n:
            break

print(t[i - 1][j - 1])




