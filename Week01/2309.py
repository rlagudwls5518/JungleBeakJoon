#일단 다 더하고 두수를 찾아서 빼보는거임 그래서 100이 나오면 그두수 인덱스 지우고 정렬 
import sys


A=[]
for i in range(9):
    A.append(int(sys.stdin.readline()))

total=sum(A)

for i in range(9):
    for j in range(i + 1, 9):
        if total - (A[i] + A[j]) == 100:
            result = [A[k] for k in range(9) if k != i and k != j]
            result.sort()
            for x in result:
                print(x)
            exit()

#굳이 안지우고 프린트만 건너띄어서 풀어도됨






#             idx1, idx2 = i, j
#             found = True
#             break
#     if found:
#         break  
# #굳이 안지우고 프린트만 건너띄어서 풀어도됨?

# if idx1 > idx2:
#     del A[idx1]
#     del A[idx2]
# else:
#     del A[idx2]
#     del A[idx1]

# A.sort()
# for x in A:
#     print(x)
    


