# import random
from datetime import datetime, timedelta

# Задание 1

def get_days_from_today(date):
    try:
        data_obj = datetime.strptime(date, "%Y-%m-%d")
        
        today = datetime.today()

        diff = today - data_obj
    
        return diff.days
    
    except ValueError:
        return "Неверный формат даты."
    
print (get_days_from_today("2021-10-09"))

# Задание 2

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)

    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа: {lottery_numbers}")


# Задание 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:  
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_to_birthday = (birthday_this_year - today).days

        if 0 <= days_to_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5:
                days_until_monday = (7 - congratulation_date.weekday()) % 7
                congratulation_date += timedelta(days=days_until_monday)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays
users = [
    {"name": "John Doe", "birthday": "1985.03.19"},
    {"name": "Jane Smith", "birthday": "1990.03.20"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список приветствий на этой неделе:", upcoming_birthdays)
