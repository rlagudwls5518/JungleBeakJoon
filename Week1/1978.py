count=int((input()))
num=map(int, input().split())

prime_count = 0


for i in num:
    # 소수 판별
    # 2부터 자기 자신-1까지 나눴을때 하나라도 나눠떨어지면 소수 아님 
    if i < 2:
        continue
    is_prime = True

    for j in range(2, i):
        if i % j ==0: #하나라도 나눠떨어지니까 소수가 아니라서 바로 브레이크
            is_prime = False
            break
    
    if is_prime:
        prime_count += 1

print(prime_count)
            

