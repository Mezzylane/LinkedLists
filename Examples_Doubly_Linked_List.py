from Doubly_Linked_List import DoublyLinkedList
import random


def main():
    
    my_list = DoublyLinkedList()
    for i in range(10):
        if i % 2 == 0:
            my_list.prepend(i)
        else:
            my_list.append(i)
    my_list.display()
    print(my_list.get_length())
    my_list.insert_after(0, -1)
    my_list.display()
    print(my_list.get_length())
    my_list.remove(1)
    my_list.display()
    my_list.display_reversed()
    my_list.insertion_sort()
    my_list.display()
    print()
    
    new_list = DoublyLinkedList()
    print(f"New list length: {new_list.get_length()}")
    for i in range(20):
        new_list.append(random.randint(1,1000))
    print("New list: ")
    new_list.display()
    print()
    new_list.insertion_sort()
    print("New list sorted (ascending): ")
    new_list.display()
    print(f"New list head: {new_list.head.data}")
    print(f"New list tail: {new_list.tail.data}")
    print()
    new_list.insertion_sort(descending=True)
    print("New list sorted (descending): ")
    new_list.display()
    print(f"New list head: {new_list.head.data}")
    print(f"New list tail: {new_list.tail.data}")
    print(f"New list length: {new_list.get_length()}")
    print()
    
    lst = DoublyLinkedList()
    word = input("Enter a word: ")
    while word != "STOP":
        if len(word) % 2 == 0:
            lst.append(word)
        else:
            lst.prepend(word)
        word = input("Enter a word: ")
    lst.display()
    lst.insertion_sort()
    lst.display()
    print()
    
    
if __name__ == "__main__":
    main()