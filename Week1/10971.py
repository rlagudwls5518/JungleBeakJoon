from itertools import permutations
import sys

city_count= int(sys.stdin.readline())
city_cost=[list(map(int, sys.stdin.readline().split())) for _ in range(city_count)]
result=1000001

# 배열을 입력받을수는 있고 
# 순열로세고 -> 돌리는데 비용이 0인경우 거르고 남은비용 더하기 

# 마지막을빼고 순열로 돌리기
# for paths in permutations(range(city_count)):
#     total_cost=0
#     valid=True
#     # 돌리는데 만약 비용이 0이면 탈락
#     for i in range(city_count-1):
#         if city_cost[paths[i]][paths[i+1]] == 0:
#             valid=False
#             break
#         else:
#             total_cost = city_cost[paths[i]][paths[i+1]]+ total_cost



# 0번 도시를 시작점으로 고정하고 나머지만 순열로 생성 -> 원순열 느낌으로
for paths in permutations(range(1, city_count)):
    total_cost = 0
    valid = True
    path = [0] + list(paths)  # 0 → ... → ... → ?

    for i in range(city_count - 1):
        c = city_cost[path[i]][path[i + 1]]
        if c == 0:
            valid = False
            break
        total_cost += c

    # 마지막도시에서 시작으로 -1은
    # 예를들어ㅏ paths =(0 1 2)  인덱스 -1은 맨뒤 , 다시처음으로 0  
    # 돌아오는 길이 있는경우와 valid가 False가 아닌경우 
    # 결국 비용이 0이 아니면서 돌아올수 있는 경우  
    if valid and city_cost[path[-1]][0] != 0:
            total_cost += city_cost[path[-1]][0]
            result=min(result, total_cost)
        

print(result)








