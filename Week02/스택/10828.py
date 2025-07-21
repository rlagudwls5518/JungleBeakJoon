import sys
input = sys.stdin.readline

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
    


N=int(input())

s= stack(N)

for _ in range(N):
    cmd = input().split()

    try:
        if cmd[0] == 'push':
            s.push(int(cmd[1]))
        elif cmd[0] == 'pop':
            print(s.pop())
        elif cmd[0] == 'size':
            print(s.count())
        elif cmd[0] == 'empty':
            print(1 if s.is_empty() else 0)
        elif cmd[0] == 'top':
            print(s.top())
    except stack.Empty:
        print(-1)
