pan_size = 8
min_size = 1
max_size = pan_size
result = 0

def alpha_to_int(alp):
    return ord(alp) - 96

def check_over(input_int):
    return input_int < min_size or input_int > max_size

way_to_move = [
    [2,1],
    [2,-1],
    [-2,1],
    [-2,-1],
    [1,2],
    [1,-2],
    [-1,2],
    [-1,-2],
]
input_text = input()
x, y = alpha_to_int(input_text[0]), int(input_text[1])

for way in way_to_move:
    if check_over(x + way[0]) == False and check_over(y + way[1]) == False:
        result += 1

print(result)