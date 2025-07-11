test_count = int(input())
results = []

for i in range(test_count):
    data = list(map(int, input().split()))
    n = data[0]         # 배열 크기
    score = data[1:]        # 나머지가 배열 데이터
    Sum=0
    for j in score:
        Sum+= j
    avg = Sum/n

    for j in range(len(score)):
        if score[j] > avg:
            score[j] = 1
        else:
            score[j] = 0

    count = sum(score)  # 평균을 넘는 학생의 수
    avg = (count/n) * 100  # 평균을 넘는 학생의 비율

    results.append(avg)
        

for i in range(len(results)):
    print(f"{results[i]:.3f}%")


    

        
    