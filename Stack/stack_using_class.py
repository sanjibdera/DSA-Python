class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, ele):
    self.stack.append(ele)
    print(ele, "Pushed into stack")
  
  def pop(self):
    if len(self.stack) == 0:
      print("Stack is empty")
    else:
      ele = self.stack.pop()
      print(ele, "Poped from stack")
  
  def peek(self):
    if len(self.stack) == 0:
      print("Stack is empty")
    else:
      print("Top element is: ", self.stack[-1])
  
  def display(self):
    if len(self.stack) == 0:
      print("Stack is empty")
    else:
      print("Stack elements are:")
      for i in reversed(self.stack):
        print(i)

s = Stack()

while True:
  print("\n Stack Operations")
  print("1. Push")
  print("2. Pop")
  print("3. Peek")
  print("4. Dispaly")
  print("5. Exit")

  chioce = int(input("Enter your choice: "))

  if chioce == 1:
    ele = input("Enter a value: ")
    s.push(ele)
  elif chioce == 2:
    s.pop()
  elif chioce == 3:
    s.peek()
  elif chioce == 4:
    s.display()
  elif chioce == 5:
    print("Program Exited")
  else:
    print("Invalid Input")
