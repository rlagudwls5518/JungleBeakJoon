import sys
# input = sys.stdin.readline

class queue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self,capacity):

        self.no=0
        self.front=0
        self.rear=0
        self.capacity=capacity
        self.que = [None] * capacity

    def __len__(self):
        return self.no
    
    def is_empty(self):
        return int(self.no <= 0)
    
    def is_full(self):
        return self.no >= self.capacity
    
    def enque(self, value):
        if self.is_full():
            raise queue.Full
        self.que[self.rear]=value
        self.rear += 1
        self.no += 1
        if self.no == self.capacity:
            self.rear =0	

    def deque(self):
        if self.is_empty():
            return -1
        value = self.que[self.front]
        self.front += 1
        self.no -= 1
        
        if self.front == self.capacity:
            self.front = 0
        return value
        
    
    def find(self, value): 
        for i in range(self.no): # 선형 검색
            idx = (i+self.front) % self.capacity
            if self.que[idx] == value:
                return idx
            return -1

    def count(self, value):
        c=0
        for i in range(self.no):
            idx = (i+self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
            return c
        

    def front_index(self):
        if self.is_empty():
            return -1
        else:
            return self.que[self.front]
        
    def back(self):
        if self.is_empty():
            return -1
        else:
            return self.que[(self.rear - 1 + self.capacity) % self.capacity]
        



N=int(sys.stdin.readline())
#N장의카드

q=queue(N)
for i in range(1,N+1):
    q.enque(i)

while q.__len__()!= 1:
    #첫번째꺼는 버리고 다음꺼는 다니 인큐
    
    q.deque()  # 첫 번째 카드 버림
    q.enque(q.deque())  # 두 번째 카드를 뒤로

print(q.front_index())
