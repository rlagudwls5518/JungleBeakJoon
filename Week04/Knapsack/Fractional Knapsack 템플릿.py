n, capacity = map(int, input().split())
items = []

for _ in range(n):
    value, weight = map(int, input().split())
    items.append((value, weight, value / weight))  # (가치, 무게, 비율)

# 비율 기준으로 정렬
items.sort(key = lambda x: x[2], reverse=True)

total_value = 0.0
for value, weight, ratio in items:
    if capacity >= weight:
        total_value += value
        capacity -= weight
    else:
        total_value += ratio * capacity  # 일부만 담기
        break

print(f"{total_value:.2f}")