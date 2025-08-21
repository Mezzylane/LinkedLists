class Node:
    def __init__(self, data=None):
        """
        Initialize a node with provided data and a next pointer set to None.
        """
        self.data = data
        self.next = None
        
        
       
class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0
        
        
    def append(self, data):
        """
        Append a node with the specified data to the end of the list.

        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to append to the list.

        Returns:
            None
        """
        new_node = Node(data)
        if self.head is None: # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
         
            
    def prepend(self, data):
        """
        Prepend a node with the specified data to the beginning of the list.

        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to prepend to the list.

        Returns:
            None
        """
        new_node = Node(data)
        if self.head is None: # List is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
          
            
    def search(self, data):
        """
        Search for a node containing the specified data.

        Public method intended for users.

        Args:
            data (Same type as Node.data): The data to search for in the list.

        Returns:
            Node or None: The node containing the specified data if found; otherwise, None.
        """
        cur_node = self.head
        while cur_node is not None: # Linear search
            if cur_node.data == data:
                return cur_node
            cur_node = cur_node.next
        return None
    
    
    def _insert_node_after(self, cur_node, new_node):
        """
        Insert the 'new_node' after 'cur_node' in the list.

        Private method intended for internal use.

        Args:
            cur_node (Node): The node currently in the list after which the new node will be inserted.
            new_node (Node): The node to insert after 'cur_node'.

        Returns:
            None
        """
        if cur_node == self.tail: # Insert after the tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = cur_node.next
            cur_node.next = new_node
    
            
    def insert_after(self, cur_data, new_data):
        """
        Insert a new node containing 'new_data' after a node with 'cur_data'.

        Public method intended for users.

        Args:
            cur_data (Same type as Node.data): The data of the existing node after which the new node will be inserted.
            new_data (Same type as Node.data): The data of the new node to insert.

        Returns:
            bool: True if insertion is successful; False otherwise.
        """
        cur_node = self.search(cur_data)
        if cur_node is not None:
            new_node = Node(new_data)
            self._insert_node_after(cur_node, new_node)
            self.length += 1
            return True
        return False
    
    
    def _remove_node_after(self, cur_node):
        """
        Remove the node immediately following the specified current node.

        Private method intended for internal use.

        Args:
            cur_node (Node): The node preceding the node to be removed. If None, the head node is removed.

        Returns:
            None
        """
        if cur_node is None: # Remove the first node
            suc_node = self.head.next
            self.head = suc_node
            if suc_node is None: # If the list is empty
                self.tail = None
        else:
            suc_node = cur_node.next.next
            cur_node.next = suc_node
            if suc_node is None: # If the current node is now the last
                self.tail = cur_node
        
                
    def remove(self, data_to_remove):
        """
        Remove the node containing the specified data from the list.

        Public method intended for users.

        Args:
            data_to_remove (Same type as Node.data): The data of the node to be removed.

        Returns:
            bool: True if removal is successful; False otherwise.
        """
        prev_node = None
        cur_node = self.head
        while cur_node is not None: # Linear search
            if cur_node.data == data_to_remove:
                self._remove_node_after(prev_node)
                self.length -= 1
                return True
            prev_node = cur_node # Track the previous node
            cur_node = cur_node.next
        return False
    
    
    def _find_insertion_position_node(self, key, descending):
        """
        Find the node after which a new node with the specified key should be inserted.

        Private method intended for internal use.

        Args:
            key (Same type as Node.data): Value of the new node to be inserted.
            descending (bool): True if sorting in descending order; False for ascending.

        Returns:
            Node: The node after which the new node should be inserted; None if it should be inserted at the head.
        """  
        cur_node_A = None
        cur_node_B = self.head
        compare = (lambda a, b: a < b) if descending else (lambda a, b: a > b)
        # Traverse the list to find the correct insertion position
        while compare(key, cur_node_B.data):
            cur_node_A = cur_node_B
            cur_node_B = cur_node_B.next
        return cur_node_A
    
    
    def insertion_sort(self, descending=False):
        """
        Sort the linked list using insertion sort.

        Public method intended for users.

        Args:
            descending (bool): True to sort in descending order; False for ascending.

        Returns:
            None
        """
        if self.head is None or self.head.next is None: # If 0 or 1 node in the list, it's already sorted
            return None
        sorted_tail = self.head # The first node is already sorted
        cur_node = self.head.next # Start sorting from the second node
        while cur_node is not None:
            next_node = cur_node.next # Save reference to the next node before moving cur_node
            # Check if cur_node is already in the correct position
            if (cur_node.data >= sorted_tail.data and not descending) or (cur_node.data <= sorted_tail.data and descending):
                sorted_tail = cur_node # Extend the sorted portion
            else:
                position_node = self._find_insertion_position_node(cur_node.data, descending)
                sorted_tail.next = next_node # Remove cur_node from its current position
                if cur_node == self.tail: # If cur_node was the tail, update self.tail
                    self.tail = sorted_tail
                # Insert cur_node at the correct position
                if position_node is None: # Insert at the head
                    cur_node.next = self.head
                    self.head = cur_node
                else: # Insert after position_node
                    cur_node.next = position_node.next
                    position_node.next = cur_node
            # Move to the next node
            cur_node = next_node
    
    
    def get_length(self):
        """
        Get the current length of the list.

        Public method intended for users.

        Returns:
            int: The length (number of nodes) of the list.
        """
        return self.length
    
    
    def display(self):
        """
        Display the list by printing the data of each node.

        Public method intended for users.

        Returns:
            None
        """
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()
