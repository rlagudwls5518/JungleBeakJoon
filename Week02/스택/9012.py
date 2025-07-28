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
    


# 확실히 로직 이해 ㄴㄴ
T = int(sys.stdin.readline())
result_list=[]

for j in range(T):
        
    input_data = sys.stdin.readline().strip()
    s = stack(len(input_data))
    for i in input_data:
        if i == '(':
            s.push(i)

        elif i == ')':
            if s.is_empty() or s.top() == ')':
                result_list.append("No")  # 닫을 게 없으면 NO
                break
            else:
                s.pop()
            
                
    if s.is_empty():
        result_list.append("Yes")


for i in range(len(result_list)):

    print(result_list[i])


    
    
     





