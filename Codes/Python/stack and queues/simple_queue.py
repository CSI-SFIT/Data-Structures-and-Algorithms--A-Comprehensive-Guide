from collections import deque

# you can initialize a deque with a list 
numbers = deque()

# Use append to add elements
numbers.append(99)
numbers.append(15)
numbers.append(82)
numbers.append(50)
numbers.append(47)

print(numbers)


# The number that entered the queue first gets removed first and so on..
first_item = numbers.popleft()
print(first_item) # 99
print(numbers) # deque([15, 82, 50])

second_item = numbers.popleft()
print(second_item) # 15
print(numbers) # deque([82, 50])