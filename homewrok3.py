# Задание 1

from datetime import datetime

def get_days_from_today(date):
    try:
        data_obj = datetime.strptime(date, "%Y-%m-%d")
        
        today = datetime.today()

        diff = today - data_obj
    
        return diff.days
    
    except ValueError:
        return "Неверный формат даты. Используйте формат 'YYYY-MM-DD'."
    
print (get_days_from_today("2021-10-09"))



