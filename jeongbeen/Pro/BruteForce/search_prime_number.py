"""
<문제 링크>
https://programmers.co.kr/learn/courses/30/lessons/42839

<알고리즘>
- numbers 속 숫자 나누기
    - 문자열 각각을 list에 저장
- 조합 가능한 모든 경우의 수 구하기
    - from itertools import permutations 이용하기
- permutation의 결과는 다음과 같은 형태이므로 각 element를 숫자로 붙여줘야 한다.
  [('0', '1', '1'), ('1', '0', '1'), ...] → [0, 1, 101, 10, 11, 110]
- 조합 list의 각 element마다 소수 여부 판별하기
    - 소수 : 약수가 1과 자기 자신(n)뿐
        ```python
        def is_prime_number(n):
        	if n < 2:
        			return False
        	for i in range(2,n):
        		if n % i == 0:
        			return False
        	return True
        ```
"""


from itertools import permutations

def is_prime_number(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    # numbers 속 숫자 나누기
    numList = [num for num in numbers]

    wholePermu = list()
    # 조합 가능한 모든 경우의 수 구하기
    for a in range(1, len(numList) + 1):
        wholePermu.extend(list(permutations(numList, a)))

    # wholePermu = [('0',), ('1',), ('1',), ('0', '1'), ('0', '1'), ('1', '0'),
    #               ('1', '1'), ('1', '0'), ('1', '1'), ('0', '1', '1'), ('0', '1', '1'),
    #               ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]


    # join 함수 : 리스트에 있는 요소들을 합쳐서 하나의 문자열로 바꾼다.
    for i in range(len(wholePermu)):
        wholePermu[i] = int(''.join([b for b in wholePermu[i]]))
    # wholePermu = [0,1,1,1,1,10,11,10,11,11,11,101,110,101,110]


    # 중복되는 조합을 제거하기 위해 중간에 잠시 set 타입으로 변경했다.
    wholePermu = list(set(wholePermu))
    # wholePermu = [0, 1, 101, 10, 11, 110]


    answer = list()

    # 조합 list의 각 element마다 소수 여부 판별하기
    for elem in wholePermu:
        if is_prime_number(elem):
            answer.append(elem)


    return len(answer)


# 실제 시작은 여기서부터
if __name__ == "__main__":
    numbers = "011"
    print(solution(numbers))