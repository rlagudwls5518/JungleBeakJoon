count=int((input()))
num=map(int, input().split())

prime_count = 0

for i in num:

    if i < 2:
        continue
    is_prime = True

    for j in range(2, i):
        if i % j ==0:
            is_prime = False
            break
    
    if is_prime:
        prime_count += 1

print(prime_count)

            

