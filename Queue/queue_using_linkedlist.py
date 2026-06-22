class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
  
  def enqueue(self):
    data = input("Enter an element: ")
    new_node = Node(data)

    if self.rear is None:
      self.front = new_node
      self.rear = new_node
    else:
      self.rear.next = new_node
      self.rear = new_node
    print(data, "inserted into queue")

  def dequeue(self):
    if self.front is None:
      print("Queue is empty")
    else:
      data = self.front.data
      self.front = self.front.next
      if self.front is None:
        self.rear = None
      print(data, "removed from queue")
  
  def display(self):
    if self.front is None:
      print("Queue is empty")
    else:
      temp = self.front
      print("Queue elements are: ")
      while temp is not None:
        print(temp.data)
        temp = temp.next
  
  def peek(self):
    if self.front is None:
      print("Queue is empty")
    else:
      print("Front element is: ", self.front.data)
  
q = Queue()
while True:
  print("1. Enqueue")
  print("2. Dequeue")
  print("3. Front")
  print("4. Display")
  print("5. Exit")
  c = int(input("Enter your chioce: "))

  if c == 1:
    q.enqueue()
  elif c == 2:
    q.dequeue()
  elif c == 3:
    q.peek()
  elif c == 4:
    q.display()
  elif c == 5:
    print("Program Exited")
    break
  else:
    print("Invalid Input")