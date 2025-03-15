"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

user_list = [
	{'first_name': 'Альбина', 'last_name': 'Дейне', 'job': 'ВИТА', 'age': 25, 'number_phone': '+7(999)-123-22-22'},
	{'first_name': 'Олег', 'last_name': 'Ефимов', 'job': 'Пристав', 'age': 27, 'number_phone': '+7(989)-777-23-22'},
	{'first_name': 'Дмитрий', 'last_name': 'Ткаченко', 'job': 'РЖД', 'age': 25, 'number_phone': '+7(988)-111-22-33'},
	{'first_name': 'Валерия', 'last_name': 'Тарасева', 'job': 'РЖД', 'age': 23, 'number_phone': '+7(989)-156-22-77'},
	{'first_name': 'Ричард', 'last_name': 'Кэтсвил', 'job': 'Домохозяин', 'age': 1.5,
	 'number_phone': '+7(900)-007-12-44'}
]


def main(lst):
	with open('files_csv/export.csv', 'w', encoding='utf-8') as file:
		fields = ['first_name', 'last_name', 'job', 'age', 'number_phone']
		writer = csv.DictWriter(file, fields, delimiter=';')

		writer.writeheader()
		for user in lst:
			writer.writerow(user)


if __name__ == "__main__":
	main(user_list)
