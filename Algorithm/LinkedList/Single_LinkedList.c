#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

int ListLength(struct ListNode *head) {
    struct ListNode *current = head;
    int count = 0;

    while(current != NULL) {
        count++;
        current = current->next;
        // pointer 구조체에 접근할 때는, '->'를 사용해야 한다.
        // 일반적인 구조체에 접근할 때는, '.'를 사용해야 한다.
    }

    return count;
}

void InsertLinkedList(struct ListNode **head, int data, int position) {
    int k = 1;
    struct ListNode *p, *q, *newNode;

    newNode = (struct ListNode*)malloc(sizeof(struct ListNode));

    if(!newNode) {  // 메모리의 에러를 확인
        printf("Memory Error!");
        return;
    }

    newNode->data = data;
    newNode->next = NULL;
    p = *head;

    if(position == 1) {
        newNode->next = p;
        *head = newNode;
    } else {
        while((p != NULL) && (k < position-1)) {
            k++;
            q = p;
            p = p->next;    // q 다음 노드가 p
        }
        if(p == NULL) {     // 마지막에 노드를 삽입하는 경우
            q->next = newNode;
        } else {            // 중간에 노드를 삽입하는 경우
            newNode->next = p;
            q->next = newNode;
        }
    }
}

void DeleteLinkedList(struct ListNode **head, int position) {
    int k = 1;
    struct ListNode *p, *q;

    if(*head == NULL) {
        printf("List Empty!!");
        return;
    }

    p = *head;

    if(position == 1) {
        *head = (*head)->next;
        free(p);
        return;
    } else {
        while((p != NULL) && (k < position-1)) {
            k++;
            q = p;
            p = p->next;
        }

        if(p == NULL)
            printf("Position does not exist");
        else {
            q->next = p->next;
            free(p);
        }
    }
}

int main() {
    struct ListNode *L = NULL;

    InsertLinkedList(&L, 10, 1);
    InsertLinkedList(&L, 20, 2);
    InsertLinkedList(&L, 30, 3);

    printf("Length of List : %d\n", ListLength(L));

    struct ListNode *temp = L;
    printf("List contents after insertion :");

    while(temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");

    DeleteLinkedList(&L, 2);

    printf("Delete the Seconde Node\n");
    printf("Length of List : %d", ListLength(L));

    temp = L;
    printf("List after Deletion :");

    while(temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    while(L != NULL) {
        temp = L;
        L = L->next;
        free(temp);
    }

    return 0;
}