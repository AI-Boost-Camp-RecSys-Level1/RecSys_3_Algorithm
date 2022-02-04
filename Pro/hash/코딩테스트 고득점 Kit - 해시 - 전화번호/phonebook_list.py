'''
<출처 링크>
https://programmers.co.kr/learn/courses/30/lessons/42577
'''

# 내 풀이
# 효율성 테스트에서 오답이 발생.
def solution_mine(phone_book):
    tmp = sorted(phone_book)
    
    for idx, x in enumerate(tmp):
        for idy, y in enumerate(tmp):
            if idx >= idy:
                continue
            if y.find(x) == 0:
                return False
    return True

############################################################33

# 정답 풀이.
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

############################################################

parameters = [
    ["119", "97674223", "1195524421"],
    ["123","456","789"],
    ["12","123","1235","567","88"]
]
answers = [
    False,
    True,
    False
]
for phone_book, answer in zip(parameters, answers):
    grading = (solution(phone_book) == answer)
    print(f'pass? {"yes" if grading else "no"}')