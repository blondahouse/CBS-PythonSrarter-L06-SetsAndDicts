while True:
    library_length = input('Enter library length (non negative integer): ')
    try:
        range(1, 10).index(int(library_length))
    except ValueError:
        print('Error message: Wrong input, try again')
    else:
        library_length = int(library_length)
        break

links_library = dict()

while library_length:
    library_length -= 1
    key_input = input('Enter short link: ')
    value_input = input('Enter full link: ')
    links_library[key_input] = value_input

print(links_library)

check_key = input('Enter short link to get long link: ')

print(f'short link is: {check_key}\n'
      f'long link is: {links_library[check_key]}')
