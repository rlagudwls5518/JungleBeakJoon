test_count = int(input())
results = []

for i in range(test_count):
    data = list(map(int, input().split()))
    n = data[0]         # 배열 크기
    score = data[1:]        # 나머지가 배열 데이터
    sum=0
    for j in score:
        sum+= j
    avg = sum/n
    results.append(avg)
        
for i in range(len(results)):
    print(f"{results[i]:.2f}")  

    

        
    