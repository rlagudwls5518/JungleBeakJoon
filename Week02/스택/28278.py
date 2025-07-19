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

    def is_empty(self): #4번 조건
        return self.ptr == 0
    
    def is_full(self):
        return self.ptr >= self.capacity
    
    def push(self, value): # 1번 조건
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
        
    def top(self): # 5번 조건
        if self.is_empty():    
            return -1
            
        return self.stk[self.ptr-1]
    
    def find(self, value): # 2번 조건
        for i in range(self.ptr):
            if self.stk[i] == value:
                return self.stk[:self.ptr]
            
        return -1

    def count(self): #3번조건 
        return self.ptr



#N = 명령

n = int(input())
s = stack(n)  # 최대 n번 push 가능하므로 capacity = n으로 설정

for _ in range(n):
    cmd = input().split()

    try:
        if cmd[0] == '1':
            s.push(int(cmd[1]))
        elif cmd[0] == '2':
            print(s.pop())
        elif cmd[0] == '3':
            print(s.count())
        elif cmd[0] == '4':
            print(1 if s.is_empty() else 0)
        elif cmd[0] == '5':
            print(s.top())
    except stack.Empty:
        print(-1)

