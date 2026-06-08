class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
  
  def push(self):
    data = input("Enter the element: ")
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node
    print(data, "pushed into stack ")
  
  def pop(self):
    if self.top == None:
      print("Stack is Empty")
    else:
      ele = self.top.data
      self.top = self.top.next
      print(ele, "popped from stack")
  
  def peek(self):
    if self.top == None:
      print("Stack is empty")
    else:
      print("Top element is: ", self.top.data)
  
  def display(self):
    if self.top == None:
      print("Stack is empty")
    else:
      temp = self.top
      print("Stack elements are: ")
      while temp is not None:
        print(temp.data)
        temp = temp.next

s = Stack()
while True:
  print("Stack Operations: ")
  print("1. Push")
  print("2. Pop")
  print("3. Peek")
  print("4. Display")
  print("5. Exit")

  choice = int(input("Enter chioce: "))
  if choice == 1:
    s.push()
  elif choice == 2:
    s.pop()
  elif choice == 3:
    s.peek()
  elif choice == 4:
    s.display()
  elif choice == 5:
    print("Program Exited")
    break
  else:
    print("Invalid Choice")