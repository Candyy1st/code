list_book = ['Book1', 'Book2', 'Book3', 'Book4']
print(f'Daftar Buku = , {list_book}')

print('\nUsing for + in =')
for book in list_book:
    print(book)

print(f'\nShowing some index = {list_book[1], list_book[3]}')

print('\nInsert to list Using Append = list_book.append("Book5")')
{list_book.append("Book5")}
print(list_book)

print('\nClear list')
list_book.clear()
for i in range(0, len(list_book)):
    print(list_book)

print('\nReplace 1st Element')
list_book = ['Book1', 'Book2', 'Book3', 'Book4']
list_book[0] = '1st Book'
print(list_book)

print('\nTake 2nd Element')
book = list_book.pop(1)
for i in range(0, len(list_book)):
    print(list_book[i])

print('\nPicked up book')
print(book)
