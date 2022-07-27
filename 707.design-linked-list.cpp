/*
 * @lc app=leetcode id=707 lang=cpp
 *
 * [707] Design Linked List
 */

// @lc code=start
#include <cstddef>
#include <iostream>
class MyLinkedList {
public:
    
    struct ListNode
    {
        int val;
        ListNode* next;
        ListNode(): val(0), next(nullptr) {};
        ListNode(int x): val(x), next(nullptr) {};
        ListNode(int x, ListNode* node): val(x), next(node) {};
        
    };

    MyLinkedList() {
        _size = 0; 
        _dummyHead = new ListNode(-1);
    }
    
    int get(int index) {
        if (index >= _size) return -1;
        ListNode* cur = _dummyHead->next;  
        while (index > 0){
            --index;
            cur = cur->next;
        }
        return cur->val;
    }
    
    void addAtHead(int val) {
        ListNode* post = _dummyHead->next;
        ListNode* newNode = new ListNode(val, post);
        _dummyHead->next = newNode;
        ++_size;
    }
    
    void addAtTail(int val) {
        ListNode* newNode = new ListNode(val);
        ListNode* curNode = _dummyHead;
        while (curNode->next) curNode = curNode->next;
        curNode->next = newNode;
        ++_size;
    }
    
    void addAtIndex(int index, int val) {
        if (index > _size) return;
        if (index == _size) return addAtTail(val);
        ListNode* prev = _dummyHead;
        while (index > 0){
            --index;
            prev = prev->next;
        }
        ListNode* post = prev->next;
        ListNode* newNode = new ListNode(val, post);
        prev->next = newNode;
        ++_size;
    }
    
    void deleteAtIndex(int index) {
        if (index >= _size) return;
        ListNode* prev = _dummyHead;
        while (index > 0) {
            prev = prev->next;
            --index;
        }
        ListNode* deletedNode = prev->next;
        prev->next = deletedNode->next;
        deletedNode->next = nullptr;
        delete deletedNode;
        --_size;
    }

    void printMyLinkedList() {
        auto cur = _dummyHead->next;
        while (cur) {
            std::cout << cur->val << " -> ";
            cur = cur->next;
        }
        std::cout << "NULL. ";
        std::cout << "Size: " << _size << std::endl;
    }
    private:
        int _size;
        ListNode* _dummyHead;
};


//int main() {
//    MyLinkedList* myLinkedList = new MyLinkedList();
//    myLinkedList->printMyLinkedList();
//
//    myLinkedList->addAtHead(1);
//    myLinkedList->printMyLinkedList();
//
//    myLinkedList->addAtTail(3);
//    myLinkedList->printMyLinkedList();
//
//    myLinkedList->addAtIndex(1, 2);    // linked list becomes 1->2->3
//    myLinkedList->printMyLinkedList();
//    
//    int ret1 = myLinkedList->get(1);              // return 2
//    std::cout << "Get: " << ret1 << std::endl;
//    myLinkedList->printMyLinkedList();
//    
//    myLinkedList->deleteAtIndex(1);    // now the linked list is 1->3
//    myLinkedList->printMyLinkedList();
//
//    int ret2 = myLinkedList->get(1);              // return 3
//    std::cout << "Get: " << ret2 << std::endl;
//    myLinkedList->printMyLinkedList();
//
//    myLinkedList->deleteAtIndex(1);    // now the linked list is 1->3
//    myLinkedList->printMyLinkedList();
//}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
// @lc code=end

