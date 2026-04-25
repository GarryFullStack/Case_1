
from datetime import datetime

# Шаблон для преобразования цифры в звезды
def print_digit(digit):
    patterns = {
        "0": ['****','*  *','*  *','*  *','****'],
        '1': ['   *',' * *','   *','   *','   *'],
        '2': ['****','   *','****','*   ','****'],
        '3': ['****','   *','****','   *','****'],
        '4': ['*  *','*  *','****','   *','   *'],
        '5': ['****','*   ','****','   *','****'],
        '6': ['****','*   ','****','*  *','****'],
        '7': ['****','   *',' *  ','*   ','*   '],
        '8': ['****','*  *','****','*  *','****'],
        '9': ['****','*  *','****','   *','****']
    }
    return patterns.get(str(digit))

# Функция вывода всех цифр в одну линию
def print_digits(digits):
    # Поочерёдно получаем каждую строчку каждой цифры
    rows = [[print_digit(digit)[i] for digit in digits] for i in range(5)]

    # Проходим по каждому ряду и соединяем цифры в одну строку
    for row in rows:
        print('    '.join(row))

# Вспомогательные функции
def get_day_of_week(date_str):
    date = datetime.strptime(date_str, "%d.%m.%Y")
    return date.weekday()

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# Основная логика программы
def main():
    # Запрашиваем дату рождения
    birth_day = input("Введите день рождения (число): ").zfill(2)
    birth_month = input("Введите месяц рождения (число): ").zfill(2)
    birth_year = input("Введите год рождения: ")

    # Полностью сформированная дата
    date_of_birth = f"{birth_day}.{birth_month}.{birth_year}"

    # Конвертируем дату в объект DateTime
    date_obj = datetime.strptime(date_of_birth, "%d.%m.%Y")

    # Результаты обработки даты
    day_number = get_day_of_week(date_of_birth)
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    leap_status = "был високосным" if is_leap_year(int(birth_year)) else "не был високосным"
    current_age = calculate_age(date_obj)

    # Вывод результатов
    print("\nРезультаты:")
    print(f"День недели: {days_of_week[day_number]}")
    print(f"Год {leap_status}.")
    print(f"Ваш возраст: {current_age} лет.\n")

    # Подготовленные цифры для отображения на табло
    numbers_for_display = birth_day + birth_month + birth_year
    print("Дата рождения в формате цифрового табло:")
    print_digits(numbers_for_display)

# Запуск главной функции
if __name__ == "__main__":
    main()