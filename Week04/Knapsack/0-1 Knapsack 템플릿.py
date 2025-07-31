# n: 물건 수, k: 배낭 최대 무게
n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]  # (무게, 가치)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
   weight, value = items[i - 1]
   
   for w in range(k + 1): 
       # 마지맞 최대가치를 출력하려면 처음부터의 가치를 모두 알아야 풀수 있다 
       # 그래서 무게가 0인것부터 차곡차곡쌓아나가다가 마지막 무게가 K일때를 찾는거지
        
       if weight > w: # 1번 
           dp[i][w] = dp[i - 1][w]  # 못 담음
       else: # 2번 1), 2) 둘다고려
           dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp[n][k])  # 최대 가치 출력