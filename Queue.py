from Singly_Linked_List import SinglyLinkedList



class Queue(SinglyLinkedList):
    """
    Queue (FIFO) implementation using a SinglyLinkedList object.
    The end of the queue corresponds to the tail of the SinglyLinkedList.
    """
    def enqueue(self, data):
        """
        Place a node with the specified data at the end of the queue.
        
        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to add to the queue.
            
        Returns:
            None
        """
        self.append(data)
    
    
    def dequeue(self):
        """
        Dequeue the node and return its data from the beginning of the queue.
        
        Public method intended for users.

        Raises:
            IndexError: If the queue is empty.

        Returns:
            Same type as Node.data: The data of the removed node.
        """
        if self.head is None:
            raise IndexError("Dequeue from empty queue.")
        dequeued_item = self.head.data
        self.head = self.head.next
        if self.head is None: # Queue is empty
            self.tail = None
        self.length -= 1
        return dequeued_item
    
    
    def peek(self):
        """
        Return the data of the node at the beginning of the queue without removing it.
        
        Public method intended for users.

        Raises:
            IndexError: If the queue is empty.

        Returns:
            Same type as Node.data: The data at the beginning of the queue.
        """
        if self.head is None:
            raise IndexError("Peek into empty queue.")        
        return self.head.data
    
    
    def is_empty(self):
        """
        Check whether the queue is empty.

        Public method intended for users.

        Returns:
            bool: True if the queue is empty; otherwise, False.
        """
        return self.length == 0
    
        
    def get_length(self):
        """
        Get the current number of elements in the queue.

        Public method intended for users.

        Returns:
            int: The number of nodes present in the queue.
        """
        return self.length
    