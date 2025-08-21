from Singly_Linked_List import SinglyLinkedList



class Stack(SinglyLinkedList):
    """
    Stack (LIFO) implementation using a SinglyLinkedList object.
    The top of the stack corresponds to the head of the SinglyLinkedList.
    """
    def push(self, data):
        """
        Push a node with the specified data onto the top of the stack.
        
        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to add to the stack.
            
        Returns:
            None
        """
        self.prepend(data)
        
        
    def pop(self):
        """
        Pop the node and return its data from the top of the stack.
        
        Public method intended for users.

        Raises:
            IndexError: If the stack is empty.

        Returns:
            Same type as Node.data: The data of the removed node.
        """
        if self.head is None:
            raise IndexError("Pop from empty stack.")
        popped_item = self.head.data
        self.head = self.head.next
        if self.head is None: # Stack is empty
            self.tail = None
        self.length -= 1
        return popped_item
    
    
    def peek(self):
        """
        Return the data of the node at the top of the stack without removing it.
        
        Public method intended for users.

        Raises:
            IndexError: If the stack is empty.

        Returns:
            Same type as Node.data: The data at the top of the stack.
        """
        if self.head is None:
            raise IndexError("Peek into empty stack.")        
        return self.head.data
    
    
    def is_empty(self):
        """
        Check whether the stack is empty.

        Public method intended for users.

        Returns:
            bool: True if the stack is empty; otherwise, False.
        """
        return self.length == 0
    
        
    def get_length(self):
        """
        Get the current number of elements in the stack.

        Public method intended for users.

        Returns:
            int: The number of nodes present in the stack.
        """
        return self.length    
