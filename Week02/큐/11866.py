import sys
from collections import deque
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
        








queue = deque()
answer = []

n, k = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)

while queue: # 덱을써서 k번째 자리전가지 다빼서 제거하고 다시넣음
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")

