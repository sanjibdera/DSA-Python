def linear_search(arr, key):
  for i in range(len(arr)):
    if arr[i] == key:
      return i
  return -1

arr = [8, 4, 12, 3, 7, 19, 6]
key = 6
result = linear_search(arr, key)
if result == -1:
  print("Element not found")
else:
  print("Element found at" , result + 1 , "position")