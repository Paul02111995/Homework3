import random
from datetime import datetime
# Задание 1

def get_days_from_today(date):
    try:
        data_obj = datetime.strptime(date, "%Y-%m-%d")
        
        today = datetime.today()

        diff = today - data_obj
    
        return diff.days
    
    except ValueError:
        return "Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
    
print (get_days_from_today("2021-10-09"))

# Задание 2

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
        return []  # Исправлен отступ и добавлен пробел

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")

