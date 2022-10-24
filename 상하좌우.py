from re import U


n = int(input())
x = 0
y = 0

for i in input().split():
    if i == "L":
        if y - 1 >= 0:
            y = y - 1
    elif i == "R":
        if y + 1 < n:
            y = y + 1
    elif i == "U":
        if x - 1 >= 0 :
            x = x - 1
    elif i == "D":
        if x + 1 < n:
            x = x + 1

print(x+1, y+1)