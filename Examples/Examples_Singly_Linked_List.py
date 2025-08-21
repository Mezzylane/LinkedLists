from LinkedLists.Singly_Linked_List import SinglyLinkedList
import random


def main():
    
    my_list = SinglyLinkedList()
    for i in range(15):
        if i % 2 == 0:
            my_list.prepend(i)
        else:
            my_list.append(i)
    my_list.display()
    my_list.insert_after(0, -1)
    my_list.display()
    print(my_list.get_length())
    my_list.remove(1)
    print(my_list.tail.data)
    print(my_list.get_length())
    my_list.insertion_sort()
    my_list.display()
    print(my_list.tail.data)
    my_list.remove(14)
    my_list.display()
    print(my_list.tail.data)
    print()
    
    new_list = SinglyLinkedList()
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
    
    
if __name__ == "__main__":
    main()