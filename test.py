import random

print('Hello world!')
print('Welcome to new world.')
print(1+2)

numbers = [random.randint(1, 100) for _ in range(10)]
sorted_numbers = sorted(numbers)

print("Unsorted numbers:", numbers)
print("Sorted numbers:", sorted_numbers)