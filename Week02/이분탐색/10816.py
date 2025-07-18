
# 가지고 있다는 갯수를 어떻게 넘겨줄 것인가????
# 카운트가 되긴 하는데 
# 내 생각은 탐색 알고리즘으로 찾으면 +1해서 리스트에 저장해서 출력인데 
# 그런데 이분탐색은 타겟 숫자가 여러개가 있으면 다찾아주나? 
# 아니래 하나만 찾아준대 처음 발견한 인덱스만 

# 그럼 함수를 수정해야하지않나
# 뭐 인덱스 가장 오른쪽이랑 왼쪽빼면 개수 나온다는데 이거맞나?
# 이분 탐색으로 풀 필요가 전혀없는 문제인데... 딕셔너리로 푸는 것이 더 낫다


# 이렇게 풀었다가 시간초과났는디 입력갯수땜시그런가 아 이중포문써서 50만개*50만개 어후 ㅋㅋ


import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 1. A 안에 있는 숫자 개수 세기 (직접 딕셔너리로)
count = {}
#존재 확인 → 없으면 초기화 → 있으면 +=1
for num in A:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# 2. B의 각 숫자에 대해 A에서 몇 번 나왔는지 출력
for target in B:
    if target in count:
        print(count[target], end=' ')
    else:
        print(0, end=' ')



