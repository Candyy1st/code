"""
Testing Perulangan
"""

total = 10
books_read = 0
print('Mom said : "You must reading 10 books"')

# Using For
for books_read in range(1,11):
    print(f'Buku ke-{books_read} sudah dibaca')

#U Using While
while books_read < total:
    books_read = books_read + 1
    print(f'Buku ke-{books_read} sudah dibaca')

print(f'Buku yang sudah dibaca = {books_read}')