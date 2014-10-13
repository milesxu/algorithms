#include <iostream>
#include <functional>

struct Node
{
    Node *next;
    int value;
};

void reverse1(Node **head)
{
    if (*head == nullptr) return;
    Node *cur = (*head)->next, *pre = *head, *succ;
    while (cur)
    {
        succ = cur->next;
        cur->next = pre;
        pre = cur;
        cur = succ;
    }
    (*head)->next = nullptr;
    *head = pre;
}

void reverse2(Node *&head)
{
    Node *pre = nullptr;
    while(head)
    {
        Node *temp = head;
        head = head->next;
        temp->next = pre;
        pre = temp;
    }
    head = pre;
}

Node *reverse3(Node *head)
{
    if (head == nullptr || head->next == nullptr)
        return head;
    Node *succ = head->next;
    head->next = nullptr;
    Node *temp = reverse3(succ);
    succ->next = head;
    return temp;
}

Node *reverse4(Node *head, Node *pre = nullptr)
{
    if (head == nullptr) return pre;
    Node *temp = head->next;
    head->next = pre;
    return reverse4(temp, head);
}

void reverse5(Node *&head)
{
    std::function<Node* (Node*&)> reverse = [&](Node *&head){
        Node *succ = head->next;
        if (succ)
        {
            Node *temp = reverse(succ);
            succ->next = head;
            return temp;
        }
        return head;
    };
    if (head)
    {
        Node *rhead = reverse(head);
        head->next = nullptr;
        head = rhead;
    }
}

void ListOutput(Node * const head)
{
    Node *temp = head;
    while(temp) {
        std::cout << temp->value << " ";
        temp = temp->next;
    }
    std::cout << std::endl;
}

int main()
{
    Node *head = nullptr;
    for (int i = 0; i < 9; ++i)
    {
        Node *temp = new Node;
        temp->next = head;
        temp->value = i;
        head = temp;
    }
    ListOutput(head);
    reverse1(&head);
    ListOutput(head);
    reverse2(head);
    ListOutput(head);
    Node *temp = reverse3(head);
    ListOutput(temp);
    temp = reverse4(temp);
    ListOutput(temp);
    reverse5(temp);
    ListOutput(temp);
    return 0;
}
