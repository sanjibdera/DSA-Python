class Queue:
  def __init__(self):
    self.queue = []
  
  def enqueue(self):
    ele = input("Enter an element: ")
    self.queue.append(ele)
    print(ele, "inserted into queue")
  
  def dqueue(self):
    if len(self.queue) == 0:
      print("Queue is empty")
    else:
      ele = self.queue.pop(0)
      print(ele, "removed from queue")
  
  def front(self):
    if len(self.queue) == 0:
      print("Queue is empty")
    else:
      print("Front element is ", self.queue[0])
  
  def display(self):
    if len(self.queue) == 0:
      print("Queue is empty")
    else:
      print("Queue elements are: ")
      for i in self.queue:
        print(i)


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
    q.dqueue()
  elif c == 3:
    q.front()
  elif c == 4:
    q.display()
  elif c == 5:
    print("Program Exited")
    break
  else:
    print("Invalid Input")