# 영식이의 4개로부터 11을 덧셈으로  @+@+@+@=11 이런느낌으로 
# 어떻게 이분탐색이쓰이는걸까
# 어떤길이를 x로 잘랐을때 만들 수 있는 랜선의 수가 N개이상이면 , x보다 더 긴 일이도 시도해볼 수 있다
# 반대로 N개보다 적으면 x보다 짧은 길이만 가능

#최소길이는 1 이고 최대길이는 입력값중에 제일 긴 길이?

import sys
K, N = map(int,sys.stdin.readline().split())
length=[]

for i in range(K):
    length.append(int(sys.stdin.readline()))


def is_possible(cut_len):
    return sum(line // cut_len for line in length) >= N

def bin_search(a): 
    pl = 1
    pr = max(a)

    while pl<=pr:
        middle=(pl+pr)//2
        if is_possible(middle):
            result = middle
            pl=middle+1
            
        else:
            pr=middle-1
    return result

print(bin_search(length))
