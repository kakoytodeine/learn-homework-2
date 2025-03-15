"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
	with open('files_txt/referat.txt', 'r', encoding='utf-8') as file:
		content = file.read()
		length_file = len(content)
		word_cnt = len([word for word in content.split()])
		replacement = content.replace('.', '!')
		print(length_file)
		print(word_cnt)
		with open('files_txt/referat2.txt', 'w', encoding='utf-8') as file2:
			file2.write(replacement)


if __name__ == "__main__":
	main()
