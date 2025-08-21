from LinkedLists.Deque import Deque
import random


def main():
    
    deque = Deque()
    for i in range(10):
        if i % 2 == 0:
            deque.push_front(random.randint(1,1000))
        else:
            deque.push_back(random.randint(1,1000))
    deque.display()
    print(deque.pop_front())
    deque.display()
    print(deque.pop_back())
    deque.display()
    print(deque.peek_front())
    print(deque.peek_back())
    print(deque.get_length())
    print(deque.is_empty())
    for i in range(deque.get_length()):
        print(deque.pop_back(), end=" ")
    print()
    print(deque.is_empty())
    # deque.peek_back()
    
    
if __name__ == "__main__":
    main()