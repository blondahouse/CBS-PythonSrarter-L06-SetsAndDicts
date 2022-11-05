long_string = input('Enter a long string of words separated by space: ')

split_string = long_string.split()
set_of_words = set(split_string)
count_dict = {}

for element in split_string:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

print(count_dict)