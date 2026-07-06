count = {}
arr = [1,1,3,3,4,4,4,6]

for i in arr:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)