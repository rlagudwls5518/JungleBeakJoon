# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
import sys

N, M =map(int, sys.stdin.readline().split())

# 예를 들어 3, 2이라고해보자
# 1부터 3까지 자연수중에서 중복없이 2개를 고른 수열
1,2
2,3
1,3
# 3가지?

# def backtrack(현재상태):
#     if 종료조건:               # ex) 길이가 N만큼 됐다면
#         정답 저장
#         return

#     for 후보 in 가능한_선택들:
#         if 조건에 맞다면:      # ex) 아직 안 쓴 숫자라면
#             상태 저장         # ex) path.append(), visited[i] = True
#             backtrack(업데이트된상태)
#             상태 복구         # ex) path.pop(), visited[i] = False


nums = [i for i in range(1, N+1)]
visited=[False]*N
path=[]


def backtrack():
    if len(path) == M:
        print(*path)
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i]=True
        path.append(nums[i])

        backtrack()
        path.pop()
        visited[i] = False

backtrack()