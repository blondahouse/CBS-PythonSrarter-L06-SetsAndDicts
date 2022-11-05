first_string = input('Enter first string: ')
second_string = input('Enter second string: ')

first_set = set(first_string)
second_set = set(second_string)

print(f'intersection set is: {first_set & second_set}')
