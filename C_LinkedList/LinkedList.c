#include <stdio.h>
#include <stdlib.h>

// 노드 구조체 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data);
int search(int data);
void freeList();
void printList();
void insertFront(int data); 
void insertEnd(int data);
void deleteNode(int data);


int main(){
	insertEnd(10);
    insertEnd(20);
    insertFront(5);
    insertEnd(30);

    printList(); // 5 -> 10 -> 20 -> 30 -> NULL

    deleteNode(20);
    printList(); // 5 -> 10 -> 30 -> NULL

    if (search(10)) {
        printf("10을 찾았습니다!\n");
    } else {
        printf("10이 리스트에 없습니다.\n");
    }

    freeList(); // 메모리 정리
    return 0;


}

// 리스트의 헤드 포인터(전역변수)
Node* head = NULL;

Node* createNode(int data)
{
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = NULL;
	
	return newNode;
}

int search(int data)
{
	Node* current = head;
	while (current != NULL)
	{
		if (current->data == data)
		{
			return 1;
		}
		current = current->next;
	}
	
	return 0;
}

void insertFront(int data)
{
	Node* newNode = createNode(data);
	newNode->next = head;
	head = newNode;
}

void freeList()
{
	Node* current = head;
	while (current != NULL)
	{
		Node* next = current->next;
		free(current);
		current = next;
	}
	
	head = NULL;
}

void printList()
{
	Node* current = head;
	while (current != NULL)
	{
		printf("%d -> ", current->data);
    current = current->next;
	}
	
	printf("NULL\n");
}

void insertEnd(int data)
{
	Node* newNode = createNode(data);
	
	if (head == NULL)
	{
		head = newNode;
		return;
	}
	
	Node* current = head;
	while (current->next != NULL)
	{
		current = current->next;
	}
	current->next = newNode;
}

void deleteNode(int data)
{
	Node* current = head; // 지울 노드
	Node* prev = NULL; // 지울 노드의 이전 노드
	
	// current가 마지막 노드가 아니고 현재 데이터가 지우고 싶은 값이 아니라면, 계속 다음으로 넘어가기
	while (current != NULL && current->data != data)
	{
		prev = current;
		current = current->next;
	}
	
	// 만약 while문 이후에 current가 NULL이라면, 지우고자 하는 데이터가 없다는 뜻
	if (current == NULL)
	{
		printf("값 %d를 찾을 수 없습니다.\n", data);
    return;
	}
	
	if (prev == NULL)
	{
		// prev가 NULL이라는건, 삭제할 노드가 첫번째 노드인 경우 : 즉, 한 번도 이동한 적 없음
		head = current->next;
	}
	else
	{
		// 삭제할 노드가 중간이나 끝에 있는 경우 : 이전 노드의 next가 current의 다음 노드를 가리키도록 변경
		prev->next = current->next;
	}
	
	free(current); // 메모리 해제!
}