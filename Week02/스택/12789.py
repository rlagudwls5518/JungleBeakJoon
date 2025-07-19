import sys
# input = sys.stdin.readline

class stack:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity):
        self.stk=[None] * capacity
        self.capacity = capacity
        self.ptr =0
    
    def __len__(self):
        return self.ptr

    def is_empty(self): 
        return self.ptr == 0
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, value): 
        if self.is_full():
            raise stack.Full
        else:
            self.stk[self.ptr]=value
            self.ptr+=1

    def pop(self):
        if self.is_empty():
            raise stack.Empty
        else:
            self.ptr-=1
            return self.stk[self.ptr]
        
    def top(self): 
        if self.is_empty():    
            return -1
            
        return self.stk[self.ptr-1]
    
    def find(self, value): 
        for i in range(self.ptr):
            if self.stk[i] == value:
                return self.stk[:self.ptr]     
        return -1

    def count(self): 
        return self.ptr
    
    def sum_(self):
        sum=0
        for i in range(self.ptr):
            sum+=self.stk[i]
        return sum
    



N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
s_1=stack(N)
s_2=stack(N)
result=stack(N)
next_num=1

for num in reversed(nums):
    s_1.push(num)

while True:
    if s_1.top() == next_num:
        s_1.pop()
        next_num += 1

    elif s_2.top() == next_num:
        s_2.pop()
        next_num += 1

    elif s_1.count() > 0:
        # 아직 대기열에 사람이 있으면 보조 스택으로 보내기
        s_2.push(s_1.pop())

    else:
        # 아무데서도 꺼낼 수 없고 끝나지 않음 → 실패
        print("Sad")
        break

    if next_num > N:
        print("Nice")
        break
    
