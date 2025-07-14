# 앞에서부터 각자리 차가 커야지만 최대값이나오는디
# 그롬 그냥 내림차순아님?
# 아니지? 애초에 절대값의 합이면 제일큰수, 제일 작은수, 두번재큰수, 두번째로 작은수.... 
# 이렇게 해서 더하념된다ㅓ?.
# 정수의 순서를 적절히 바꿔서
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
# 
#  

data_count = int(input())
A=list(map(int, input().split()))



A.sort()
sum=0
for i in range(len(A)):
    for j in range(len(A) - 1, -1, -1):
        sum=sum+abs(A[i]-A[j])
print(A)

