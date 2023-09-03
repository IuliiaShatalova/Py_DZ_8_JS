def add_person(person):
    data = open("Dict.txt", 'a', encoding='utf-8')
    data.writelines(person)
    data.writelines('\n')
    data.close()


def show_all():
    data = open('Dict.txt', 'r', encoding='utf-8')
    for line in data:
        print(line[:-1])
    data.close()


def search_element(name):
    with open('Dict.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if name in line.split():
                print(line)
                break
            else:
                print('Такого нет')


def delite_contact(delname):
    with open ('Dict.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
        with open ('Dict.txt', 'w', encoding='utf-8') as data:
            for line in lines:
                if line.find(delname) == -1:
                    data.write(line)


def change_contact():
    old_cont = input('Введите контакт для изменения ')
    new_cont = input('Введите новые данные ')
    with open('Dict.txt', 'r', encoding='utf-8') as data:
        lines = data.readlines()
        with open('Dict.txt', 'w', encoding='utf-8') as data2:
            for line in lines:
                line = line.strip()
                if line == old_cont:
                    data2.write(new_cont + '\n')
                else:
                    data2.write(line + '\n')






