

input()

heights = [[int(y), x + 1] for x, y in enumerate(input().split())]
flags = [0] + [1 for x in range(len(heights))] + [0]
heights.sort()

maximum = slip_cnt = 1

for h, ix in heights:
    if slip_cnt > maximum:
        maximum = slip_cnt
        h_max = h
    flags[ix] = 0
    if flags[ix-1] and flags[ix+1]:
        slip_cnt += 1
    elif not flags[ix-1] and not flags[ix+1]:
        slip_cnt -= 1

print(maximum + 1)


















