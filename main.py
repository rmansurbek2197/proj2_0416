# 1
n = 12
s = 0
for i in range(1, n+1):
    s += i
print(s)

# 2
n = 6
f = 1
for i in range(1, n+1):
    f *= i
print(f)

# 3
nums = [2, 4, 6, 8, 10]
res = []
for x in nums:
    res.append(x * 2)
print(res)

# 4
text = "hello"
rev = ""
for c in text:
    rev = c + rev
print(rev)

# 5
nums = [1, 3, 5, 7]
total = 0
for x in nums:
    total += x
print(total)

# 6
n = 10
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

# 7
text = "banana"
count = 0
for c in text:
    if c == "a":
        count += 1
print(count)

# 8
nums = [5, 2, 9, 1]
mx = nums[0]
for x in nums:
    if x > mx:
        mx = x
print(mx)

# 9
nums = [5, 2, 9, 1]
mn = nums[0]
for x in nums:
    if x < mn:
        mn = x
print(mn)

# 10
for i in range(5):
    row = ""
    for j in range(5):
        row += "*"
    print(row)
