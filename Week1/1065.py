num= int(input())
count=0

if num<100:
    count=num
else:
    count=99
    for i in range(100,num+1):
        nums= list(map(int,str(i)))
        if nums[1]-nums[0] == nums[2]-nums[1]:
            count+=1

print(count)
    



       
