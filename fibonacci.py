 fibonacci

#top to bottom 
storage = {}
def fibonacci(num):
  if num in storage.keys():
    return storage[num]
  else: 
    if num < 2:
      storage[num] = num
      return num
    else:
      x = fibonacci(num - 1)
      y = fibonacci(num -2)
      storage[num - 1] = x 
      storage[num - 2] = y
      storage[num] = x + y
      return x + y

print(fibonacci(100))
print(storage)
