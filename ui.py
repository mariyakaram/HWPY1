
from logger import input_data, print_data, delete_data, edit_data 

def interface():
    print("Добрый день! Вы попали в справочник ГК \n1 - запись данных \n2 - вывод данных \n3 - удаление данных \n4 - правка данных")
    command = int(input('Введите число '))

    while command != 1 and command !=2 and command !=3 and command !=4:
        print("Неправильный ввод")
        command = int(input('Введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        delete_data()
    elif command == 4:
        edit_data()
        
