from Queue import Queue
import random


def main():
    
    queue = Queue()
    print(queue.is_empty())
    for i in range(10):
        queue.enqueue(random.randint(1,1000))
    queue.display()
    print(queue.dequeue())
    queue.display()
    print(queue.peek())
    print(queue.get_length())
    print(queue.is_empty())
    
    
if __name__ == "__main__":
    main()