import sys

N=int(sys.sys.stdin.readline)

pos =[0]*N # 열배치
flag_a =[False]*N # 각행에 있는지 
flag_b =[False]*15 # 우측상향 대각선에 있는지
flag_c =[False]*15 # 좌측하향 대각선에 았는지
# 왜 대각선은 15칸이지?-> 2n-1 대각선 갯수 -1은 겹치는거하나뺌
# 행이랑 열이랑 확실한 구분 아직 미숙

def put():
    for i in range(N):
        print(f'{pos[i]:2}',end='')
    print()


# 왜 대각선에 i+j랑 i-j+7인지 -> y=x, y=-x 일차함수 그래프? 

def set(i):
    for j in range(N):
        if (not flag_a[j] and not flag_b[i+j] and not flag_c[i-j+7]):
            pos[i]=j

            if i ==7:
                put()
            else:
                flag_a[j]=flag_b[i+j]=flag_c[i-j+7] =True
                set(i+1)
                flag_a[j]=flag_b[i+j]=flag_c[i-j+7] =False

set(0)
