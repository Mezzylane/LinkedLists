class Node:
    def __init__(self, data=None):
        """
        Initialize a node with provided data and two pointers (previous and next) set to None.
        """
        self.data = data
        self.previous = None
        self.next = None


        
class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
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
            new_node.previous = self.tail
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
            self.head.previous = new_node
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
    
    
    def __insert_node_after(self, cur_node, new_node):
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
            new_node.previous = self.tail
            self.tail = new_node
        else:
            suc_node = cur_node.next
            new_node.next = suc_node
            new_node.previous = cur_node
            cur_node.next = new_node
            suc_node.previous = new_node
    
            
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
            self.__insert_node_after(cur_node, new_node)
            self.length += 1
            return True
        return False
    
    
    def __remove_node(self, cur_node):
        """
        Remove the specified node.

        Private method intended for internal use.

        Args:
            cur_node (Node): The node to be removed.

        Returns:
            None
        """
        suc_node = cur_node.next
        prev_node = cur_node.previous
        if suc_node is not None: # cur_node is not the tail
            suc_node.previous = prev_node
        else: 
            self.tail = prev_node
        if prev_node is not None: # cur_node is not the head
            prev_node.next = suc_node
        else:
            self.head = suc_node
    
                
    def remove(self, data_to_remove):
        """
        Remove the node containing the specified data from the list.

        Public method intended for users.

        Args:
            data_to_remove (Same type as Node.data): The data of the node to be removed.

        Returns:
            bool: True if removal is successful; False otherwise.
        """
        node_to_remove = self.search(data_to_remove)
        if node_to_remove is not None:
            self.__remove_node(node_to_remove)
            self.length -= 1
            return True
        return False
    
    
    def __find_insertion_position_node(self, cur_node, descending):
        """
        Find the node after which cur_node should be inserted.

        Private method intended for internal use.

        Args:
            cur_node (Node): The node to be inserted.
            descending (bool): True if sorting in descending order; False for ascending.

        Returns:
            Node: The node after which cur_node should be inserted; None if it should be inserted at the head.
        """ 
        position_node = cur_node.previous # Start searching from the previous node
        # Find the correct position for cur_node
        if descending:
            while position_node is not None and position_node.data < cur_node.data:
                position_node = position_node.previous
        else:
            while position_node is not None and position_node.data > cur_node.data:
                position_node = position_node.previous
        return position_node
    
    
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
        cur_node = self.head.next # Start sorting from the second node
        # Everything left of the cur_node is sorted
        while cur_node is not None:
            next_node = cur_node.next # Store reference to the next node (before moving cur_node)
            position_node = self.__find_insertion_position_node(cur_node, descending)              
            # If cur_node is already in the correct position, move to the next node
            if cur_node.previous == position_node:
                cur_node = next_node
                continue
            # Remove cur_node from its current position
            cur_node.previous.next = next_node
            if next_node is not None: # If cur_node is not the tail
                next_node.previous = cur_node.previous
            else: # If cur_node was the tail, update self.tail
                self.tail = cur_node.previous
            # Insert cur_node in the correct position
            if position_node is None: # Insert at the head
                cur_node.next = self.head
                cur_node.previous = None
                self.head.previous = cur_node
                self.head = cur_node
            else: # Insert after position_node
                cur_node.next = position_node.next
                cur_node.previous = position_node
                position_node.next.previous = cur_node
                position_node.next = cur_node
            # Move to the next node (the one originally after cur_node)
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
        Display the list by printing the data of each node starting from the head.

        Public method intended for users.

        Returns:
            None
        """
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()
    
        
    def display_reversed(self):
        """
        Display the list by printing the data of each node strating from the tail.

        Public method intended for users.

        Returns:
            None
        """
        cur_node = self.tail
        while cur_node is not None:
            print(cur_node.data, end=" ")
            cur_node = cur_node.previous
        print()    
        