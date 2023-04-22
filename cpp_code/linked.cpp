#include<iostream>
using namespace std;

class Node {

    //Data Member are below:
    public:
    int data;
    Node* next;

    //constructor
    Node(int data) {
        this->data  = data;
        this->next = NULL;
    }

};

void insertAtHead(Node* &head, int d) {
        //step 1: create new node
        Node* newNode = new Node(d);
        //step2: set next ptr to head node
        newNode->next = head;
        //step3: head update;
        head = newNode;
}

void insertAtTail(Node* &tail, int d) {
        //step 1: cration of Node
        Node* newNode = new Node(d);
        //step2: 
        tail->next = newNode;
        //step3: head update;
        tail = newNode;
}

void insertAtPosition(Node* &head, int pos, int d) {
    //TODO: tail updation, while inserting node at the end
    //TODO: validate that position should 
    //be atmax 1 more than current Lenght of LL
    if(pos == 1) {
        insertAtHead(head,d);
    }
    else {
        //Step1: cration of New Node
        Node* newNode = new Node(d);

        //step2: 
        Node* prev = head;
        int t = pos-2;
        while(t--)
        {
            prev= prev->next;
        }

        //step3: connections update
        newNode->next = prev->next;
        prev->next = newNode;
    }
}

void traverse(Node* &head) {
    Node* temp = head;
    while(temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp ->next;
    }
    cout << endl;
}


void deleteNode(Node* &head, int target, int pos) {

    //empty list
    if(head == NULL)
        return;

    Node* temp = head;
    Node* prev = NULL;
    if(target == temp->data && pos == 1){
        head  = head ->next;
        temp -> next = NULL;
        delete temp;
    }
    else{

        while(temp != NULL && temp->data != target) {
            prev = temp;
            temp = temp->next;
        }
        //here we are assuiming that we have found the element

        if(temp == NULL)
            {
                cout << "NOde node found" << endl;
                return;
            }
        prev -> next = temp->next;
        temp ->next = NULL;
        delete temp;

    }

}

int getLength(Node* &head) {
    Node* temp = head;
    int len = 0;
    while(temp != NULL)
    {
        len++;
        temp = temp->next;
    } return len;
}

Node* reverse(Node* &head) {

    if(head == NULL)
    {
        cout << "List is Empty" << endl;
        return head;
    }

    Node* curr = head;
    Node* prev = NULL;

    while(curr != NULL) {
        //to keep track of list ahead of curr
        Node* forward = curr -> next;
        //change curr link and connect it to prev node
        curr->next = prev;

        //aage badho
        prev = curr;
        curr = forward;
    }

    return prev;
}

Node* getMiddle(Node* head) {
    Node* slow = head;
    Node* fast = head;

    while(fast != NULL && fast ->next != NULL) {
        //2 step
         fast = fast -> next ->next;
         //1 step
         slow = slow -> next;
    }
    return slow;
}

Node* reverseInK(Node* &head, int k) {
    //empty list
    if(head == NULL)
    return NULL;

    Node* curr = head;
    Node* next = curr -> next;
    Node* prev = NULL;
    int count = 0;

    //Step 1: reverse first k nodes
    while(curr != NULL && count < k) {
        next = curr -> next;
        curr -> next = prev;

        prev = curr;
        curr = next; 
        count++;
    }

    //next pointer will be pointing at the head of the remaining list
    
    if(next != NULL){
        //step2:recursion will get ans for remaining list
        Node* rem = reverseInK(next, k);
        //step3: connection list in step 1 and step 3
        head -> next = rem;
    }
        
    //step 4: return head of entire list
    return prev;
}

int main() {

    //object creation

    Node* b = new Node(1);
    Node* head = b;
    Node* tail = b;

    traverse(head);

    insertAtTail(tail,2);
    insertAtTail(tail,3);
    insertAtTail(tail,4);
    insertAtTail(tail,5);
    insertAtTail(tail,7);
    insertAtTail(tail,8);
    insertAtTail(tail,9);

    traverse(head);
    insertAtPosition(head, 6, 6); // pos, no
    traverse(head);

    //Node* head2 = NULL;
    //deleteNode(head2, 13, 1);
    traverse(head);
    cout << getLength(head) << endl;
   
    cout<<"middle "<<endl;
    traverse(head);
    cout<<getMiddle(head)->data<<endl;

    cout<<"reverse"<<endl;
    head=reverse(head);
    traverse(head);

    cout<<"Reverse with k group"<<endl;
    head = reverseInK(head, 3);
    traverse(head);

    return 0;
}