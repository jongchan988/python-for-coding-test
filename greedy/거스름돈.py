# 정수 입력값
n = int(input())
c = 0

# 사이즈 리스트 정의
coin_size = [500, 100, 50, 10]
# 사이즈 정렬(내림차순) -> 옵션
coin_size.sort(reverse=True)
for size in coin_size:
    # 나눈 몫 만큼 총 개수에 더해준다.
    c += n // size
    # 정수 입력값을 동전 크기로 나눈 나머지를 다음 루프의 거스름돈으로 쓴다.
    n = n % size
print(c)