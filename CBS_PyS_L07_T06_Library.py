from CBS_PyS_L07_T00_Definitions import *

books = dict()

# Creating menu
menu_items = ['add book',
              'remove book',
              'Show library sorted by book',
              'Show library sorted by author']

c = 1
while c:
    menu_list(menu_items)
    c = dialogue('\tEnter your choice (integer): ', len(menu_items))
    print()

    match c:
        case 1:
            author = input('Enter author name: ')
            book = input('Enter book name: ')
            if author not in books:
                books[author] = [book]
            else:
                books[author].append(book)
        case 2:
            author = input('Enter author name: ')
            book = input('Enter book name: ')
            if author not in books or book not in books[author]:
                print('The book you want to remove is not in the library')
            else:
                if len(books[author]) == 1:
                    del books[author]
                else:
                    books[author].remove(book)
        case 3:
            # books = {'qwer': ['ty', 'ui', 'op'], 'asdf': ['gh', 'jk'], 'zxcv': ['bn']}
            books_list = []
            for i in books:
                for ii in books[i]:
                    books_list.append((ii, i))
            books_sorted_list = sorted(books_list)
            for i in books_sorted_list:
                print(f'{i[0]} : {i[1]}')
            print()
        case 4:
            # books = {'qwer': ['ty', 'ui', 'op'], 'asdf': ['gh', 'jk'], 'zxcv': ['bn']}
            sorted_by_authors = {k: v for k, v in sorted(books.items())}
            # print(sorted_authors)
            for i in sorted_by_authors:
                for ii in sorted_by_authors[i]:
                    print(f'{i} : {ii}')
            print()
        case 0:
            break

