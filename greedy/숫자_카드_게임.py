n, m = map(int, input().split())
max_value = 0
for i in range(n): 
    min_value = min(list(map(int, input().split())))
    max_value = max_value if max_value > min_value else min_value

print(max_value)