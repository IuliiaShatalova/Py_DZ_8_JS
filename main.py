from Interface import *
from WorkWithFile import *

while True:
    interface()
    command = int(input('Введите команду: '))
    if command == 1:
        person = input('Введите данные пользователя: ')
        add_person(person)
    elif command == 2:
        show_all()
    elif command == 3:
        name = input('Введите элемент для поиска: ')
        search_element(name)
    elif command == 4:
        delname = input('Введите фамилию для удаления')
        delite_contact(delname)
    elif command == 5:
        change_contact()
    elif command == 6:
        break
    else:
        print("Ввод не корректен")