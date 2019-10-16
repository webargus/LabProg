
n = int(input())
peaks = [int(i) for i in input().split()]

valleys = list(set(peaks))
cuts = [0 for i in range(len(valleys))]
for i in range(len(valleys)):
    cutting = False
    for height in peaks:
        if height > valleys[i]:
            if not cutting:
                cutting = True
                cuts[i] = cuts[i] + 1
        else:
            cutting = False
print(max(cuts) + 1)

