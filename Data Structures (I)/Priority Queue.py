""" 
Priority Queue

A priority queue is a special type of queue in which each element is associated with a priority value. And, elements are served 
on the basis of their priority. That is, higher priority elements are served first.

However, if elements with the same priority occur, they are served according to their order in the queue.

Assigning Priority Value

Generally, the value of the element itself is considered for assigning the priority. For example,

The element with the highest value is considered the highest priority element. However, in other cases, we can 
assume the element with the lowest value as the highest priority element.

We can also set priorities according to our needs.
"""

# Priority Queue implementation in Python

# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child, and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    # Swap the element to delete with the last element
    array[i], array[size - 1] = array[size - 1], array[i]

    # Remove the last element (the one we want to delete)
    array.pop()

    # Rebuild the heap
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))

"""
Priority Queue Applications
Some of the applications of a priority queue are:

° Dijkstra's algorithm
° for implementing stack
° for load balancing and interrupt handling in an operating system 
° for data compression in Huffman code

"""
