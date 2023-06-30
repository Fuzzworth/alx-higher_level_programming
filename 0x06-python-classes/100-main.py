#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(10)
sll.sorted_insert(2)
sll.sorted_insert(-3)
sll.sorted_insert(34)
sll.sorted_insert(4)
sll.sorted_insert(-5)
sll.sorted_insert(0)
sll.sorted_insert(8)
sll.sorted_insert(7)
print(sll)
