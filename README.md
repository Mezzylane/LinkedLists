# Linked Lists

Objects SinglyLinkedList(), DoublyLinkedList(), Stack(), Queue(), Deque() built in Python.

## Installation

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Running Examples

To run example scripts, use the `-m` option so Python treats `LinkedLists` as a package.  

## Objects and Their Usage

### Singly Linked List

The `SinglyLinkedList` class can be found in the `Singly_Linked_List.py` file. It uses `Node` objects to represent elements within the list.

#### Node Attributes:

    - data: The data associated with the node.
    - next: The pointer to the next node in the list.

#### SinglyLinkedList Attributes:
    
    - head: The first node in the list.
    - tail: The last node in the list.
    - length: The number of nodes in the list.

#### Public Methods:

    - append(data): Adds a node with the specified data to the end of the list.

    - prepend(data): Adds a node with the specified data to the beginning of the list.
    
    - search(data): Finds a node containing the specified data.
        Returns: The Node if found; otherwise, None.

    - insert_after(cur_data, new_data): Inserts a new node containing 'new_data' after a node with 'cur_data'.
        Returns: True if insertion is successful; False otherwise.

    - remove(data): Removes the node containing the specified data from the list.
        Returns: True if removal is successful; False otherwise.

    - insertion_sort(descending=False): Sorts the linked list using insertion sort.
        Pass True (or descending=True) to sort in descending order.

    - get_length(): Obtains the current length of the list.
        Returns: An integer representing the number of nodes.

    - display(): Prints the data of each node, from head to tail.
___    

### Doubly Linked List

The `DoublyLinkedList` class can be found in the `Doubly_Linked_List.py` file. It uses `Node` objects to represent elements within the list. The `Node` objects has a pointer to the previous node.

#### Node Attributes:

    - data: The data associated with the node.
    - previous: The pointer to the previous node in the list.
    - next: The pointer to the next node in the list.

#### DoublyLinkedList Attributes:
    
    - head: The first node in the list.
    - tail: The last node in the list.
    - length: The number of nodes in the list.

#### Public Methods:

    - append(data): Adds a node with the specified data to the end of the list.

    - prepend(data): Adds a node with the specified data to the beginning of the list.
    
    - search(data): Finds a node containing the specified data.
        Returns: The Node if found; otherwise, None.

    - insert_after(cur_data, new_data): Inserts a new node containing 'new_data' after a node with 'cur_data'.
        Returns: True if insertion is successful; False otherwise.

    - remove(data): Removes the node containing the specified data from the list.
        Returns: True if removal is successful; False otherwise.

    - insertion_sort(descending=False): Sorts the linked list using insertion sort.
        Pass True (or descending=True) to sort in descending order.

    - get_length(): Obtains the current length of the list.
        Returns: An integer representing the number of nodes.

    - display(): Prints the data of each node, from head to tail.

    - display_reversed(): Prints the data of each node, from tail to head.
___

### Stack

The `Stack` class can be found in the `Stack.py` file. It is derived from the `SinglyLinkedList` class.

#### Public Methods:

    - push(data): Pushes a node with the specified data onto the top of the stack.

    - pop(): Pops the node from the top of the stack.
        Raises: IndexError if the stack is empty.
        Returns: The data of the popped node.

    - peek(): Peeks at the data at the top of the stack without removing it.
        Raises: IndexError if the stack is empty.
        Returns: The data at the top of the stack.

    - is_empty(): Checks whether the stack is empty.
        Returns: True if the stack is empty; otherwise, False.

    - get_length(): Obtains the current length of the stack.
        Returns: An integer representing the number of nodes in the stack.
___

### Queue

The `Queue` class can be found in the `Queue.py` file. It is derived from the `SinglyLinkedList` class.

#### Public Methods:

    - enqueue(data): Place a node with the specified data at the end of the queue.

    - dequeue(): Dequeue the node from the beginning of the queue.
        Raises: IndexError if the queue is empty.
        Returns: The data of the dequeued node.

    - peek(): Peeks at the data at the beginning of the queue without removing it.
        Raises: IndexError if the queue is empty.
        Returns: The data at the beginning of the queue.

    - is_empty(): Checks whether the queue is empty.
        Returns: True if the queue is empty; otherwise, False.

    - get_length(): Obtains the current length of the queue.
        Returns: An integer representing the number of nodes in the queue.
___

### Deque

The `Deque` class can be found in the `Deque.py` file. It is derived from the `DoublyLinkedList` class.

#### Public Methods:

    - push_front(data): Pushes a node with the specified data to the front of the deque.

    - push_back(data): Pushes a node with the specified data to the back of the deque.

    - pop_front(): Pops the node from the front of the deque.
        Raises: IndexError if the deque is empty.
        Returns: The data of the popped node.

    - pop_back(): Pops the node from the back of the deque.
        Raises: IndexError if the deque is empty.
        Returns: The data of the popped node.

    - peek_front(): Peeks at the data at the front of the deque without removing it.
        Raises: IndexError if the deque is empty.
        Returns: The data at the front of the deque.

    - peek_back(): Peeks at the data at the back of the deque without removing it.
        Raises: IndexError if the deque is empty.
        Returns: The data at the back of the deque.

    - is_empty(): Checks whether the deque is empty.
        Returns: True if the deque is empty; otherwise, False.

    - get_length(): Obtains the current length of the deque.
        Returns: An integer representing the number of nodes in the deque.
___

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)