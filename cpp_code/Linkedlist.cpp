#include<iostream>
using namespace std;

class node(){
    public:
    //data
    int data=0;
    //addresso of the next node
    node* next;
    //last node point to the null
    node(ind d){
        this->data = d;
        this-> next = NULL;
    }
}
int main(){
    // linked list
    //an liner str data type
    
    node* 1st = new node(3);
    cout<< 1st->data <<endl;

    return 0;
}