import json

def to_make_values(link_to_file: str) -> dict:
    """
    Функция преобразует данные к виду id: value
    """
    f = {}
    try:
        with open(link_to_file) as file:
            data = json.load(file)
            try:
                for i in data['values']:
                    f[i['id']] = i['value']
            except Exception as e:
                if type(e) == KeyError:
                    print(f'В файле values.json нет ключа с названием {e}')
                else:
                    print(e)
        return f
    except Exception as e:
        if type(e) == FileNotFoundError:
            print("Указан неверный адрес расположения файла values.json")
        else:
            print(e)
    


def report(link_to_file_tests:str, values: dict) -> str:
    """ Принимаем 2 аргумента, путь до файла tests.json и преобразованный словарь. 
        Создаём ф-ю update. Её задача сформировать конечный результат для файла report.json
        Далее всё просто.
        Парсим данные из файла tests.json и сохраняем их в переменную.
        Преобразуем дынные с помощью ф-и update
    """
    if not link_to_file_tests:
        return f'Нет пути до файла tests.json'

    def update(global_val: dict, dict_by_tests:dict):
        for i in dict_by_tests:
            u = i['id'] 
            if 'value' in i:
                i['value'] = global_val[u]
            if 'values' in i:
                update(global_val, i['values'])

    try:
        with open(link_to_file_tests) as file:
            data = json.load(file)
            update(values, data['tests'])
            return data
    except Exception as e:
        print(e)


def safe(link_to_save: str, data: dict):
    """
        Ф-я принимает путь по которому будет сохранен файл report.json и записывает в него данные
    """
    if link_to_save:
        full_name_file = link_to_save + 'report.json'
    else:
        full_name_file = 'report.json'
    with open(full_name_file, 'w') as file1:
        json.dump(data, file1, indent=4)
    return f'Файл сохранен по пути {full_name_file}'


if __name__ == '__main__':
    values = None
    while True:
        values = to_make_values(input('Введите полный путь до файла values.json\n'))
        if values:
            break

    data = report(input("Введите путь до файла tests.json\n"), values)
    print(safe(input("Введите путь где будет сохранён файл report.json\n"), data))
