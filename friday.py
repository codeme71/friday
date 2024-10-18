import datetime

def day_of_week(year, month, day):
  """
  Определяет день недели по заданной дате.

  Args:
    year: Год (например, 2025)
    month: Месяц (например, 11 для ноября)
    day: День (например, 14)

  Returns:
    Строка с названием дня недели (например, "Понедельник")
  """

  date = datetime.date(year, month, day)
  day_name = date.strftime("%A") # Форматирует день недели в текстовом формате
  return day_name

# Пример использования
year = 2025
month = 11
day = 14

day_name = day_of_week(year, month, day)
print(f"Дата {year}-{month}-{day} - это {day_name}")







