import datetime

def day_of_week(year, month, day):
  """
  Определяет день недели по заданной дате.

  Args:
    year: Год (например, 2023)
    month: Месяц (например, 12 для декабря)
    day: День (например, 25)

  Returns:
    Строка с названием дня недели (например, "Понедельник")
  """

  date = datetime.date(year, month, day)
  day_name = date.strftime("%A") # Форматирует день недели в текстовом формате
  return day_name

# Пример использования
year = 2025
month = 12
day = 25

day_name = day_of_week(year, month, day)
print(f"Дата {year}-{month}-{day} - это {day_name}")


