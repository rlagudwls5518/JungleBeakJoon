Test_count = int(input())
results = []
for i in range(Test_count):
    R, S = input().split()
    R = int(R)
    S = str(S)

    result = ""
    for i in range(len(S)):
        result += S[i] * R
    results.append(result) 

for i in range(len(results)):
    print(results[i]) 
