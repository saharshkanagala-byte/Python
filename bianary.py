def binary_search(arr, left, right, target):
  if right >= left:
    mid = (left + right) // 2
    print(f"Step {left}-{right}: checking elements at index {mid}: {arr[mid]}")
    if arr[mid] == target:
      return mid
  elif arr[mid] > target:
    print(f'Step {left}-{right}: {target} is smaller than {arr[mid]}, searching in the left half')
    return binary_search(arr, left, mid - 1, target)
  else:
    print(f'Step {left}-{right}: {target} is greater than {arr[mid]}, searching in the right half')  
    return binary_search(arr, mid + 1, right, target)
  return -1

animals = ['dog', 'cat', 'fish', 'kitten', 'pig']
target = 'fish'
print(f"searching for {target} in list {animals}")
result = binary_search(animals, 0, len(animals) -1 , target)

if result == -1:
  print(f'{target} not in list')
else:
  print(f"{target } is found at {result}")
