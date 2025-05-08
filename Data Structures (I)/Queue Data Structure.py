# Queue implementation in Python

class Queue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the queue
    def enqueue(self, data):

        if (self.tail == self.k - 1):
            print("The queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data

    # Delete an element from the queue
    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.head + 1
            return temp

    def printQueue(self):
        if(self.head == -1):
            print("No element in the queue")

        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Your Queue object will be instantiated and called as such:
obj = Queue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printQueue()

----------------------------------------------CODE-ABOVE-WITH-COMMENT------------------------------------------


# Queue implementation in Python with inline explanations

class Queue():

    def __init__(self, k):
        self.k = k  # Maximum size of the queue
        self.queue = [None] * k  # Preallocate a list with None values
        self.head = self.tail = -1  # Initialize head and tail pointers to -1 (empty queue)

    # Insert an element into the queue
    def enqueue(self, data):

        if (self.tail == self.k - 1):  # If tail is at last index, the queue is full (not circular)
            print("The queue is full\n")

        elif (self.head == -1):  # If queue is empty, set head and tail to 0 and insert first element
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data  # Insert data at tail

        else:
            self.tail = self.tail + 1  # Move tail to next position
            self.queue[self.tail] = data  # Insert data at new tail

    # Delete an element from the queue
    def dequeue(self):
        if (self.head == -1):  # If head is -1, the queue is empty
            print("The queue is empty\n")

        elif (self.head == self.tail):  # Only one element in the queue
            temp = self.queue[self.head]  # Store the value to return
            self.head = -1  # Reset head and tail to -1 (empty queue)
            self.tail = -1
            return temp  # Return the dequeued value

        else:
            temp = self.queue[self.head]  # Store the front value
            self.head = self.head + 1  # Move head to next element
            return temp  # Return the dequeued value

    def printQueue(self):
        if(self.head == -1):  # If queue is empty
            print("No element in the queue")

        else:
            for i in range(self.head, self.tail + 1):  # Print elements from head to tail
                print(self.queue[i], end=" ")
            print()

# Important notes: it’s a linear queue (not circular), so even after removing elements, the space is not reused. 
# When tail reaches the end (k - 1), no more elements can be added unless the queue is reset. ← just just copy this 
# message and make it comment for the Python file.
