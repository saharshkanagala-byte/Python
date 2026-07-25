def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)
  return merge(left_half, right_half)

def merge(left, right):
  result = []
  left_idx, right_idx = 0, 0 
  while left_idx < len(left) and right_idx < len(right):
    if left[left_idx][1] < right[right_idx][1]:
      result.append(left[left_idx])
      left_idx +=1 
    else:
      result.append(right[right_idx])
      right_idx += 1
  result.extend(left[left_idx:])
  result.extend(right[right_idx:])
  return result

print('Welcome to animal sorting game! ')
animal = []
while True:
  name = input('Enter a animal or type done to exit: ')
  if name == 'done':
    break

  size = int(input('Enter a size (1 - 10):'))
  animal.append((name, size))

print('Great lets help the animals line up in size')

print('Heres the lineup from smallest to largest')

sorted_list = merge_sort(animal)

for i in sorted_list:
  print(i[0])


  

