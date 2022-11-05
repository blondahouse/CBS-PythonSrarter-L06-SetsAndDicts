# first_set = input('Enter first set (integers): ')
# second_set = input('Enter second set (integers): ')
from CBS_PyS_L07_T00_Definitions import *

first_list_length_limit = 10
first_list_message = 'Yor first list is'
first_list = new_int_list(first_list_length_limit, first_list_message)
first_set = set(first_list)

second_list_length_limit = 10
second_list_message = 'Yor second list is'
second_list = new_int_list(second_list_length_limit, second_list_message)
second_set = set(second_list)

print(f'The difference between first and second list is: {first_set - second_set}')
print(f'The difference between second and first list is: {second_set - first_set}')
