w, h = map(int,input().split())

width=[0,w]#가로
height=[0,h]#세로


count=int(input())
for i in range(count):

    num,cut = map(int,input().split())

    if num==0:# 가로면 0
        height.append(cut)
    else:# 세로면 1
        width.append(cut)


width.sort()
height.sort()

max_width = max(width[i+1] - width[i] for i in range(len(width)-1))
max_height = max(height[i+1] - height[i] for i in range(len(height)-1))

print(max_height* max_width)


