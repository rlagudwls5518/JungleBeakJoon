

class Node:# 연결리스트 노드 클래스

    def __init__(self,data):
        self.data = data
        self.next = next


class LinkedList: # 연결리스트 클래스

    def __init__(self):
        self.no=0
        self.head = None
        self.current = None

    def __len__(self):
        return self.no
    
    def search(self,value): # 데이터와 같은 값이 있는지 선형 검색
        cnt=0
        ptr=self.head
        while ptr is not None:
            if ptr.data == value:
                self.current = ptr
                return ptr
            cnt += 1
            ptr = ptr.next
        
    def __contains__(self, data): # 연결리스트에 데이터가 포함되어있는지
        return self.search(data)

    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data,ptr)    
        self.no += 1

    def add_last(self, data):
        if self.head == None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None: # -> 꼬리 노드 찾아야 끝에 넣지 ptr은 꼬리노드 참조
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1
    
    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next
        self.head.no-=1

    def remove_last(self):
        if self.head == None:
            self.remove_first()
        else:
            ptr = self.head
            pre = self.head

            while ptr.next is not None:
                pre = ptr
                ptr = ptr.next

            pre.next = None
            self.current = pre 
            self.no -= 1
  
    def remove(self, p): # 노드 p를 삭제
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p: # 찾는 p가 있는지 선형검색
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -=1

    def remove_current_node(self): # 현재 노드 삭제
        self.remove(self.current)

    def clear(self): # 전체 노드 삭제 헤드 노드를 계속삭제 
        while self.head is not None:
            self.remove_first()

        self.current = None
        self.no = 0

    def next(self):# 주목노드 뒤에노드로 옮기기
        if self.current is None or self.current.next is None:
            return False
        
        self.current = self.current.next

        return True
    

    def print_current_node(self):# 주목 노드 출력
        if self.current is None:
            print("주목노드가 현재 없습니다")
        else: 
            print(self.current.data)
    
    def print(self):#모든 노드 출력
        ptr = self.head

        while ptr is None:
            print(ptr.data)
            ptr = ptr.next






