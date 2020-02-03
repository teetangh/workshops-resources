#include <iostream>
using namespace std;

struct node
{
    int data;
    struct node *next;
};

node *insertRear(node *first, int data)
{
    node *newnode = new node;
    newnode->data = data;
    newnode->next = NULL;
    if (first == NULL)
        return newnode;
    else
    {
        node *last = first;
        while (last->next != NULL)
            last = last->next;

        last->next = newnode;

        return first;
    }
}

void display(node *first)
{
    node *temp = first;
    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}
int main()
{

    int vertices;
    int edges;

    cin >> vertices >> edges;
    int v1, v2;

    node *listArray[vertices];
    for (int i = 0; i < vertices; i++)
    {
        listArray[i] = NULL;
    }

    for (int i = 0; i < edges; i++)
    {
        cin >> v1 >> v2;
        listArray[v1] = insertRear(listArray[v1], v2);
        listArray[v2] = insertRear(listArray[v2], v1);
    }

    cout << "*******" << endl;
    for (int i = 0; i < vertices; i++)
    {
        cout << i << ":";
        display(listArray[i]);
        cout << endl;
    }
}