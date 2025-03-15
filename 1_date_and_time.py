"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, time, timedelta
import locale

locale.setlocale(locale.LC_TIME, "ru_RU")


def print_days():
	date_today = date.today()
	today = date_today.strftime('%A %d %B %Y')
	delta_one_day = timedelta(days=1)
	delta_thirty_days = timedelta(days=30)
	date_yesterday = (date_today - delta_one_day).strftime('%A %d %B %Y')
	date_month_ago = (date_today - delta_thirty_days).strftime('%A %d %B %Y')
	print(f"Вчера был(а): {date_yesterday}\n"
		  f"Сегодня: {today}\n"
		  f"30 дней назад был(а): {date_month_ago}")


def str_2_datetime(date_string):
	date_dt = datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f')
	return date_dt

if __name__ == "__main__":
	print_days()
	print(str_2_datetime("01/01/20 12:10:03.234567"))
