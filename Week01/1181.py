import sys
count = int(sys.stdin.readline())

A=[]

for i in range(count):
    A.append(sys.stdin.readline().strip())



#중복 단어제거
# unique_A = []
# for word in A:
#     if word not in unique_A: # unique리스트에 word가 없으면 아래 실행
#         unique_A.append(word)
            

# 중복 제거 먼저 리스트로!
A_unique = list(set(A))

# 정렬: 길이순, 같으면 사전순
A_unique.sort(key=lambda x: (len(x), x))

# set 중복제거 순서바뀜
#sorted(정렬할_자료, key=정렬기준, reverse=True or False)


for i in A_unique:
    print(i)



