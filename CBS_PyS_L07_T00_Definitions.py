def new_int_list(list_length_limit, list_message):
    while True:
        list_length = input(f'Enter list length (non negative integer less then {list_length_limit}): ')
        try:
            range(1, list_length_limit).index(int(list_length))
        except ValueError:
            print('Error message: Wrong input, try again')
        else:
            list_length = int(list_length)
            break

    list_values = []
    for _ in range(list_length):
        while True:
            list_item = input(f'Enter list item #{_ + 1} (integer): ')
            try:
                int(list_item)
            except ValueError:
                print('Error message: Wrong input, try again')
            else:
                list_item = int(list_item)
                break
        list_values.append(list_item)
    print(f'\n{list_message}: {list_values}\n')
    return list_values


def menu_list(menu_items):
    for index, value in enumerate(menu_items):
        print(f'\t{index + 1}. {value}')
    print(f'\t0. Exit\n')


def dialogue(message, list_length):
    while True:
        c = input(message)
        try:
            range(list_length + 1).index(int(c))
            return int(c)
        except ValueError:
            print("\t\tError message: Wrong input, try again")

