# n = l의 개수, m = 더하는 수의 개수, k = 한 인댁스를 연속적으로 더하기가 가능한 수
n, m, k = map(int, input().split())

# n개의 개수가 담긴 리스트
l = list(map(int, input().split()))

c = 0
r = 0
# 리스트를 큰 순서대로 재 정렬한다.
l.sort(reverse = True)
for i in range(m) :
    # count 가 연속적으로 더하기가 가능한 수이거나 클 경우 2번째로 큰 수를 더하고 count를 초기화한다.
    if (c >= k) :
        r += l[1]
        c = 0
    # 결과값에 가장 큰 수를 더하고 count 를 증가시킨다.
    else:
        r += l[0]
        c += 1
print(r)
