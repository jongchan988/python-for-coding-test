# n = 입력하는 총 데이터의 개수
# m = 데이터를 반복해서 더하는 개수
# k = 한 데이터를 반복해서 더할 수 있는 개수

# n m k 입력
n, m, k = map(int, input().split())
# list data 입력
data_list = list(map(int, input().split()))

# list data 정렬
data_list.sort(reverse = True)

# 반복되는 수열의 사이즈
list_repeat_size = k+1

# 첫번째로 큰 수가 반복되는 횟수 
# 1. 수열이 반복되는 횟수에 포함되는 첫번째로 높은 수의 개수
first_data_cnt = int(m / list_repeat_size) * k
# 2. 수열 반복이 끝난 뒤 첫번째로 높은 수의 나머지 횟수
first_data_cnt += m % list_repeat_size

result = 0
# 첫번째 수의 총 합
result += first_data_cnt * data_list[0]
# 두번째 수의 총 합
result += (m - first_data_cnt) * data_list[1]
# 결과 출력
print(result)