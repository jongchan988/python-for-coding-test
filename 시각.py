n = int(input())
def check_3(i):
    h = i // (60 * 60)
    m = (i - h * (60 * 60)) // 60
    s = i - (h * (60 * 60)) - m * 60 
    if "3" in str(h) or "3" in str(m) or "3" in str(s):
        return True
    return False
result = 0

s = n * 60 * 60 + 59 * 60 + 59
for i in range(s):
    if check_3(i) == True:
        result += 1

print(result)

