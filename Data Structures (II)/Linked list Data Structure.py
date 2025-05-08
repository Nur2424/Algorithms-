# Linked list Data Structure

"""

A linked list is a linear data structure that includes a series of connected nodes. 
Each node stores the data and the address of the next node.

You have to start somewhere, so we give the address of the first node a special name called HEAD.
Also, the last node in the linked list can be identified because its next portion points to NULL.

"""

# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next     # This line moves the head pointer to the next node using linked_list.head = linked_list.head.next.


"""
Linked List Applications
Dynamic memory allocation
Implemented in stack and queue
In undo functionality of softwares
Hash tables, Graphs

"""
+






