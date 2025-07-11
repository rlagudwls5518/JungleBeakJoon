#곱셈

# B의 첫째 자리 수 부터 A와 곱한 수 출력
# 첫째자리수는 10을 나눈 나머지 
# A= int(input())  
# B = int(input()) 

# first= (B % 10) * A
# second = ((B // 10) % 10)
# third = B // 100

# print(A * (B % 10))  
# print(A * ((B // 10) % 10))  
# print(A * (B // 100))
# print(A * B)  

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 문자열로도  받을수 있음 메모리랑 시간이 더걸림
A= int(input())
B = int(input()) 
B_str = str(B)  
     
first_num = int(B_str[-1])
second_num = int(B_str[-2])
third_num = int(B_str[-3])


print(first_num*A)   
print(second_num*A)
print(third_num*A)
print(A * B)  