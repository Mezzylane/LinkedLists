from Doubly_Linked_List import DoublyLinkedList



class Deque(DoublyLinkedList):
    """
    Deque implementation using a DoublyLinkedList object.
    The front of the deque corresponds to the head of the DoublyLinkedList.
    The back of the deque corresponds to the tail of the DoublyLinkedList.
    """
    def push_front(self, data):
        """
        Push a node with the specified data to the front of the deque.
        
        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to add to the front of the deque.
            
        Returns:
            None
        """
        self.prepend(data)
        
        
    def push_back(self, data):
        """
        Push a node with the specified data to the back of the deque.
        
        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to add to the back of the deque.
            
        Returns:
            None
        """
        self.append(data)
        
        
    def pop_front(self):
        """
        Pop the node and return its data from the front of the deque.
        
        Public method intended for users.

        Raises:
            IndexError: If the deque is empty.

        Returns:
            Same type as Node.data: The data of the removed node.
        """
        if self.head is None:
            raise IndexError("Pop from empty deque.")
        popped_item = self.head.data
        self.head = self.head.next
        if self.head is None: # Deque is empty
            self.tail = None
        else:
            self.head.previous = None
        self.length -= 1
        return popped_item
    
    
    def pop_back(self):
        """
        Pop the node and return its data from the back of the deque.
        
        Public method intended for users.

        Raises:
            IndexError: If the deque is empty.

        Returns:
            Same type as Node.data: The data of the removed node.
        """
        if self.head is None:
            raise IndexError("Pop from empty deque.")
        popped_item = self.tail.data
        self.tail = self.tail.previous
        if self.tail is None: # Deque is empty
            self.head = None
        else:
            self.tail.next = None
        self.length -= 1
        return popped_item    
    
    
    def peek_front(self):
        """
        Return the data of the node at the front of the deque without removing it.
        
        Public method intended for users.

        Raises:
            IndexError: If the deque is empty.

        Returns:
            Same type as Node.data: The data at the front of the deque.
        """
        if self.head is None:
            raise IndexError("Peek into empty deque.")        
        return self.head.data
    
    
    def peek_back(self):
        """
        Return the data of the node at the back of the deque without removing it.
        
        Public method intended for users.

        Raises:
            IndexError: If the deque is empty.

        Returns:
            Same type as Node.data: The data at the back of the deque.
        """
        if self.head is None:
            raise IndexError("Peek into empty deque.")        
        return self.tail.data    
    
    
    def is_empty(self):
        """
        Check whether the deque is empty.

        Public method intended for users.

        Returns:
            bool: True if the deque is empty; otherwise, False.
        """
        return self.length == 0
    
        
    def get_length(self):
        """
        Get the current number of elements in the deque.

        Public method intended for users.

        Returns:
            int: The number of nodes present in the deque.
        """
        return self.length    
