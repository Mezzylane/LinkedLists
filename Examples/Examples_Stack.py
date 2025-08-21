from LinkedLists.Stack import Stack
import random


def main():
    
    stack = Stack()
    print(stack.is_empty())
    for i in range(10):
        stack.push(random.randint(1,1000))
    stack.display()
    print(stack.pop())
    stack.display()
    print(stack.peek())
    print(stack.get_length())
    print(stack.is_empty())
    
    
if __name__ == "__main__":
    main()