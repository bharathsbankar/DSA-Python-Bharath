#   QUEUE : last in - first out
#       for inserting append at right end using obj.append(element)
#       for removing pop at left side by obj.popleft()

from collections import deque
class Queue:
    def __init__(self,size=5):
        self.max=size
        self.queue=deque()

    def enqueue(self,element):
        if len(self.queue)<self.max:
            self.queue.append(element)
        else:
            print("can't insert element < queue is full >")

    def dequeue(self):
        if len(self.queue)!=0:
            a=self.queue.popleft()
            print(f"{a} is removed")
        else:
            print("can't remove < queue is empty >")

    def __str__(self):
        return str(self.queue)





if __name__=='__main__':
    a=Queue()
   #a.enqueue(element)
   #a.dequeue() --> remove and return element
    a.enqueue(10)
    a.enqueue(20)
    a.enqueue(30)
    print(a)
    a.dequeue()
