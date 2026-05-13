# project - CRUD operation

from pathlib import Path


def readfileandfolder():
    p = Path('')
    items = list(p.rglob('*'))

    for index, file in enumerate(items):
        if file.is_file():
            print(f'{index + 1} - {file}')


def create_file():

    readfileandfolder()

    file_name = input('Enter name of your file: ')

    p = Path(file_name)

    if p.exists():
        print('FILE ALREADY EXISTS')

    else:
        with open(file_name, 'w') as file:

            content = input('Enter your file content: ')

            file.write(content)

            print('FILE ADDED!')


def read_file():
    readfileandfolder()
    file_name = input('enter your file content:')
    p = path(file_name)
    if p.exists():
        with open(file_name, 'r' ) as file:
            print(file.read)
    else:
        print('FILE NOT FOUND!')


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

option = int(input("Enter a choice: "))

if option == 1:
    create_file()

if option ==2:
    read_file()

    