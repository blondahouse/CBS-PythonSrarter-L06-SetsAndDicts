# Name = {id: [first_name, last_name, nickname]}
# Experience = just a value, or maybe a start working year... no too difficult, just a value. Natural integer.
# Portfolio = no idea... let it be boolean
# Efficiency = just a value, maybe its smth dynamic, floating number in range [0,1]
# Techs-tack = {id: technology}
# Salary = just a value, real, floating

# So... the first man looks like
# 1: {Name: Name[1],
#     Experience: 5,
#     Portfolio: True,
#     Efficiency: 0.78,
#     Tech-stack: [Tech-stack[3], Tech-stack[4], Tech-stack[7]]
#     Salary: 156480.0}

# Shown as (if we get a person card):
# Blonskyi Oleg 'blondahouse' (id 1)
#       Experience      5 years
#       Portfolio       Exists
#       Efficiency      0.78
#       Tech-stack       - Data storage and querying
#                       - Backend Framework
#                       - Monitoring and performance tools
#       Salary          $156 480.00

# Tech-stack
Tech_stack = {1: 'Operating systems and programming languages',
              2: 'Servers and load balancing',
              3: 'Data storage and querying',
              4: 'Backend Framework',
              5: 'Frontend Framework',
              6: 'API services',
              7: 'Monitoring and performance tools',
              8: 'Business intelligence solutions',
              9: 'Behavioral and product analytics'}

person = dict()
# for i in range(26):
#     person[i] = {'Firstname': chr(97 + 25 - i) + 'Oleg',
#                  'Lastname': chr(97 + i) + 'Blonskyi',
#                  'Experience': 5,
#                  'Portfolio': True,
#                  'Efficiency': 0.78,
#                  'Tech-stack': {Tech_stack[3], Tech_stack[4], Tech_stack[7]},
#                  'Salary': 156480.0}
person[0] = {'Firstname': 'Oleg',
             'Lastname': 'Blonskyi',
             'Experience': 5,
             'Portfolio': True,
             'Efficiency': 0.78,
             'Tech-stack': {Tech_stack[3], Tech_stack[4], Tech_stack[7]},
             'Salary': 156480.0}

page_number = 1
while page_number:
    person_firstname_sorted_tuples = sorted(person.items(), key=lambda item: item[1]['Firstname'] + item[1]['Lastname'])
    person_firstname_sorted = {k: v for k, v in person_firstname_sorted_tuples}
    # print(person_firstname_sorted_tuples)
    # print(person_firstname_sorted)
    print(f'\t{"".center(38, " ").center(40, ".")}'
          f'\n\t{"main board".center(30, " ")}{"exit".center(10, " ")}'
          f'\n\t{"prev".center(10, " ")}'
          f'{f"page #{page_number:02d}".center(20, " ")}'
          f'{"next".center(10, " ")}\n\n'
          f'\t{"#id".rjust(10)}'
          f'\tfullname')

    for i in range(0 + 7 * (page_number - 1), 7 + 7 * (page_number - 1)):
        if i in range(len(person_firstname_sorted)):
            print(f'\t{str(list(person_firstname_sorted.keys())[i]).rjust(10)}',
                  f'\t{person[list(person_firstname_sorted.keys())[i]]["Firstname"]} '
                  f'{person[list(person_firstname_sorted.keys())[i]]["Lastname"]}'[0:20])
        else:
            print()

    print(f'\t',
          f'add'.center(40),
          f'\n\n\t', f'enter name or id to act'.center(40),
          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')

    main_input = input(f'\t\tEnter your choice: ')
    try:
        # list(person.values())[int(main_input)]
        person[int(main_input)]
    except (IndexError, ValueError, KeyError):
        match main_input:
            case 'prev':
                if page_number > 1:
                    page_number -= 1
            case 'next':
                if page_number <= (len(person) // 7):
                    page_number += 1
            case 'add':
                print()
                print(f'\t{"".center(38, " ").center(40, ".")}')
                print(f'\t{"New account creation".center(40, " ")}')
                print(f'\t', f'{"for id #" + str(len(person)):^20}{"back":^10}{"exit":^10}', sep='')
                print(f'\n\t', f'enter person name to create'.center(40),
                      f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                add_input = input(f'\t\tEnter person name: ')
                match add_input.lower():
                    case 'back':
                        break
                    case 'exit':
                        exit()
                person[len(person)] = {'Firstname': add_input,
                                       'Lastname': '',
                                       'Experience': 0,
                                       'Portfolio': False,
                                       'Efficiency': 0.0,
                                       'Tech-stack': {Tech_stack[3], Tech_stack[4], Tech_stack[7]},
                                       'Salary': 0.0}
            case 'exit':
                exit()
    else:
        while True:
            main_input = int(main_input)
            print()
            print(f'\t{"".center(38, " ").center(40, ".")}')
            print(f'\t',
                  f'remove'.center(20, " "),
                  "back".center(10, " "), "exit".center(10, " "), sep='')
            print()
            print(f'\t', f'Firstname\t\t'.rjust(20), f'{person[main_input]["Firstname"]}'.ljust(20), sep='')
            print(f'\t', f'Lastname\t\t'.rjust(20), f'{person[main_input]["Lastname"]}'.ljust(20), sep='')
            print()
            print(f'\t', f'Salary\t\t'.rjust(20), f'${person[main_input]["Salary"]:,.2f}', sep='')
            print(f'\t', f'Experience\t\t'.rjust(20), f'{person[main_input]["Experience"]} years'.ljust(20), sep='')
            print(f'\t', f'Portfolio\t\t'.rjust(20), f'{person[main_input]["Portfolio"]}', sep='')
            print(f'\t', f'Efficiency\t\t'.rjust(20), f'{person[main_input]["Efficiency"]:.0%}',
                  sep='')
            print(f'\t', f'Tech-stack\t\t'.rjust(20), sep='')
            for i in range(len(person[main_input]["Tech-stack"])):
                print(f'\t', f''.center(10), f'- {list(person[main_input]["Tech-stack"])[i][0:24]}'.ljust(30), sep='')
            print()
            print(f'\t', f'enter field name to edit'.center(40),
                  f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')

            edit_input = input(f'\t\tEnter your choice: ')
            match edit_input.lower():
                case 'firstname':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'Current firstname is:\t\t'.center(40, ' '),
                          f'\n\t', f'{person[main_input]["Firstname"][0:28]}'.rjust(30),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    edit_field_input = input(f'\t\tEnter new firstname: ')
                    match edit_field_input.lower():
                        case 'back':
                            break
                        case 'exit':
                            exit()
                    person[main_input]["Firstname"] = edit_field_input
                case 'lastname':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'Current lastname is:\t\t'.center(40, ' '),
                          f'\n\t', f'{person[main_input]["Lastname"][0:28]}'.rjust(30),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    edit_field_input = input(f'\t\tEnter new lastname: ')
                    match edit_field_input.lower():
                        case 'back':
                            break
                        case 'exit':
                            exit()
                    person[main_input]["Lastname"] = edit_field_input
                case 'experience':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'Current experience is:\t\t'.center(40, ' '),
                          f'\n\t', f'{person[main_input]["Experience"]} y.'.rjust(30),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    while True:
                        edit_field_input = input(f'\t\tEnter new experience: ')
                        try:
                            int(edit_field_input) if int(edit_field_input) > 0 else ValueError
                        except ValueError:
                            match edit_field_input.lower():
                                case 'back':
                                    break
                                case 'exit':
                                    exit()
                        else:
                            person[main_input]["Experience"] = edit_field_input
                            break
                case 'portfolio':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'Current portfolio existence is:\t\t'.center(40, ' '),
                          f'\n\t', f'{person[main_input]["Portfolio"]}'.rjust(30),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    while True:
                        edit_field_input = input(f'\t\tEnter new portfolio status: ')
                        try:
                            int(edit_field_input)
                        except ValueError:
                            match edit_field_input.lower():
                                case 'back':
                                    break
                                case 'exit':
                                    exit()
                                case 'false' | 'n' | '-' | 'f' | 'no' | 'non':
                                    person[main_input]["Portfolio"] = False
                                    break
                                case 'true' | 'y' | '+' | 't' | 'yes' | 'yeah':
                                    person[main_input]["Portfolio"] = False
                                    break
                        else:
                            if int(edit_field_input) < 0:
                                person[main_input]["Portfolio"] = False
                            else:
                                person[main_input]["Portfolio"] = bool(int(edit_field_input))
                            break
                case 'efficiency':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'Current efficiency rate is:\t\t'.center(40, ' '),
                          f'\n\t', f'{person[main_input]["Efficiency"]}'.rjust(30),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    while True:
                        edit_field_input = input(f'\t\tEnter new efficiency rate: ')
                        try:
                            float(edit_field_input) if 0 <= float(edit_field_input) <= 1 else ValueError
                        except ValueError:
                            match edit_field_input.lower():
                                case 'back':
                                    break
                                case 'exit':
                                    exit()
                        else:
                            person[main_input]["Efficiency"] = float(edit_field_input)
                            break
                case 'tech-stack':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'{"":^5}', f'Current tech-stack is:', sep='')
                    for i in person[main_input]["Tech-stack"]:
                        if len(i) <= 28:
                            print(f'\t', f'{"":^8}', f'{i:<30}', sep='')
                        else:
                            print(f'\t', f'{"":^8}', f'{i[0:25] + "...":<30}', sep='')
                    print(f'\n\t', f'{"":^5}', f'{"Possible values:":<30}', sep='')
                    for i in Tech_stack.items():
                        if len(i[1]) <= 25:
                            print(f'\t', f'{"":^8}', f'{i[0]:d}. {i[1]:<30}', sep='')
                        else:
                            print(f'\t', f'{"":^8}', f'{i[0]:d}. {i[1][0:22] + "...":<30}', sep='')
                    print(f'\n\t', f'enter stack IDs to set'.center(40),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    while True:
                        edit_field_input = input(f'\t\tList new stack IDs by space: ')
                        try:
                            for i in edit_field_input.strip().split():
                                # int(i) if int(i) in Tech_stack.keys() else ValueError
                                if int(i) in Tech_stack.keys():
                                    int(i)
                                else:
                                    raise ValueError
                        except ValueError:
                            match edit_field_input.lower():
                                case 'back':
                                    break
                                case 'exit':
                                    exit()
                        else:
                            person[main_input]["Tech-stack"].clear()
                            for i in edit_field_input.strip().split():
                                person[main_input]["Tech-stack"].add(Tech_stack[int(i)])
                            break
                case 'salary':
                    print(f'\n\t{"".center(38, " ").center(40, ".")}'
                          f'\n\t',
                          f'{person[main_input]["Firstname"]} '
                          f'{person[main_input]["Lastname"]}'[0:18].center(20, " "),
                          "back".center(10, " "), "exit".center(10, " "),
                          f'\n\t', f'Current salary is:\t\t'.center(40, ' '),
                          f'\n\t', f'{person[main_input]["Salary"]}'.rjust(30),
                          f'\n\t', ''.center(38, " ").center(40, "."), f'\n', sep='')
                    while True:
                        edit_field_input = input(f'\t\tEnter new salary: ')
                        try:
                            float(edit_field_input) if float(edit_field_input) >= 0 else ValueError
                        except ValueError:
                            match edit_field_input.lower():
                                case 'back':
                                    break
                                case 'exit':
                                    exit()
                        else:
                            person[main_input]["Salary"] = float(edit_field_input)
                            break
                case 'remove':
                    del person[main_input]
                    break
                case 'back':
                    break
                case 'exit':
                    exit()
