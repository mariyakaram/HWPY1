import sys
from data_create import name_data, surname_data, phone_data, adress_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберите вариант: "))

    while var != 1 and var !=2:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{adress}\n\n")

def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


    print('Вывожу данные из второго файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines
        print(*data_second)

def delete_data():
    print('Введите имя для удаления данных: \n')
    name = name_data()
    ret = []
    ret2 = []
    ret3 = []
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        flag = False
        for line in data_first:
            if line == f"{name}\n":
                flag = True
            if line == '\n':
                ret3.append(";".join(ret2))
                ret2 = []
                flag = False
            if flag == False:
                ret.append(line)
                ret2.append(line.replace("\n", ""))
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        f.writelines(ret)

    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        f.writelines(ret3)

def edit_data():
    print('Введите имя для изменения данных: \n')
    name = name_data()
 
    # создаем словарь ret
    ret = {}
    ret2 = []
    dict_key = None
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        flag = False
        for line in f.readlines():
            if line == "\n":
                flag = True
            else:
                flag = False
                if dict_key is None:
                    dict_key = line.replace("\n", "")
            
            if flag == False:
                ret2.append(line.replace("\n", ""))
            else:
                if dict_key is not None:
                    #заполняем словарь ret ключем по имени пользователя
                    ret[dict_key] = ret2

                ret2 = []
                dict_key = None

        if dict_key is not None:
            #последний раз нужно еще раз заполнить словарь, потому что в конце файла отсутвует переход
            ret[dict_key] = ret2

    if name in ret.keys():
        surname = surname_data()
        phone = phone_data()
        adress = adress_data()
        ret[name] = [name, surname, phone, adress]
    else:
        print("Имя не существует!")
        edit_data()
        
    with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
        for i in ret.values():
            f.writelines("\n".join(i))
            f.write("\n\n")

    with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
        for i in ret.values():
            f.writelines(";".join(i))
            f.write("\n")
