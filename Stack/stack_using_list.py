stack = []

def push():
  ele = input("enter a value: ")
  stack.append(ele)
  print(ele, "Pushed into stack")

def pop():
  if len(stack) == 0 :
    print("Stack is empty")
  else :
    ele = stack.pop()
    print(ele, "Poped from stack")

def peek():
  if len(stack) == 0 :
    print("Stack is empty")
  else :
    print("Top element is: ", stack[-1])

def display():
  if len(stack) == 0 :
    print("Stack is empty")
  else :
    print("Stack Elements are: ")
    for i in reversed(stack):
      print(i)

while True:
  print("\n Stack Operatins")
  print("1. Push")
  print("2. Pop")
  print("3. Peek")
  print("4. Display")
  print("5. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    push()
  elif choice == 2:
    pop()
  elif choice == 3:
    peek()
  elif choice == 4:
    display()
  elif choice == 5:
    print("Program Exit")
    break
  else:
    print("Invalid Choice")
  