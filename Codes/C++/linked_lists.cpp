#include <iostream>

using namespace std;

// user defined datatype to store an integer value and the adress of the next node
struct node
{
    int value;
    node* next = nullptr;
};

// start pointer to point to the start of the linked list
node* start = nullptr;
// endd pointer to point to the last element of the linked list
node* endd = nullptr;

// function to insert a node in a liked list
void push_back(int value)
{
    // create a node
    node* n1 = new node();
    // assign a value to the node
    n1->value = value;

    // if the list is empty create the first node and point start and end to it
    if(endd == nullptr){
        start = n1;
        endd = n1;
    }
    // if the list is not empty point the next of the current last node to the new last node, and update end   
    else{
        endd->next = n1;
        endd = n1;
    }
}

//function to add element to the start of the array
void push_front(int value)
{
    // create a node
    node* n = new node();
    // set the nodes value
    n->value = value;

    //update start
    n->next = start;
    start = n;
}

// function to delete an element of the linked list
void pop(){
    node* ptr = start;
    // if only one element is there then empyt the list
    if(start == endd){
        start = endd= nullptr;
    }
    else{
        while(ptr->next != endd){
            ptr= ptr->next;
        }
        ptr->next=nullptr;
    }
}

// function to print the elements of a linked list
void print_list(node* list_start){
    node* ptr = start;
    cout << "List = ";
    while(ptr != nullptr){
        cout << ptr->value << " ";
        ptr = ptr->next;
    }
    cout << endl;
}

int main(){

    int value;

    // inserting n elements in a linked list
    // lets insert 5 elements 
    cout << "Enter 5 elements: ";
    for(int i = 1; i <= 5; i++)
    {
        cin >> value;
        push_back(value);
    }
    // view the list
    print_list(start);

    // lets add an element to the start of the list
    cout << "Enter the value you want to add to the front: ";
    cin >> value;
    push_front(value);
    print_list(start);

    // popping a value from the list
    cout << "After Popping from the list: " << endl;
    pop();
    print_list(start);
}
