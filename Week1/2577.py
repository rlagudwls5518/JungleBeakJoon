A= int((input()))
B= int((input()))
C= int((input()))
result=[]
mul= A * B * C
mul_str= str(mul)

for i in range(10):
    result.append(mul_str.count(str(i)))


for i in range(10):
    print(result[i])