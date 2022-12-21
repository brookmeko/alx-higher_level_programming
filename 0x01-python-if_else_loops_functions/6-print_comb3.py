#!/usr/bin/python3
for num in range(0, 10):
  for num1 in range (0, 10):
    if num < num1:
        if not (num == 8 and num1 == 9):
            print('{}{},'.format(num, num1), end=" ")
        else:
            print('{}{},'.format(num, num1), end=" ")
print('')
