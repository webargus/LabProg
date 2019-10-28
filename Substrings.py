
s = input("Input the string:")

print("Using 2 loops:")
for i in range(len(s)):
    ss = ""
    for j in range(i, len(s)):
        ss += s[j]
        print(ss)
print(30*"---")

print("Using 1 loop:")
i = j = 0
ss = ""
chars = len(s)
while j < chars:
    ss += s[j + i]
    print(ss)
    i += 1
    if j + i == chars:
        i = 0
        j += 1
        ss = ""
print(30*"---")


def ss_func(s, ss="", i=0, j=0):
    chars = len(s)
    ss += s[j + i]
    print(ss)
    if j == chars - 1:
        return
    i += 1
    if j + i == chars:
        i = 0
        j += 1
        ss = ""
    ss_func(s, ss, i, j)


print("Using 0 loops:")
ss_func(s)
