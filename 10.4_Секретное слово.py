n = input()
m = int(input())
lst = []
s1, s2, s3  = {}, {}, {}
for i in n:
    s1[i] = s1.get(i,0) +1
for i in range(m):
    l = input().split(":")
    lst.append(l)

s2 = {i[0]: i[1] for i in lst}
for k, v in s1.items():
    for key, value in s2.items():
        value = int(value)
        if v == value:
            s3.setdefault(k, key)
result = []
for i in n:
    for k,v in s3.items():
        if i == k:
            i == v
            result.append(v)
print(*result, sep = "")  # Pycharm не считывает знак * ?