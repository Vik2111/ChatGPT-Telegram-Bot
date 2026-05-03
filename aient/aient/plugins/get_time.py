import pytz
import datetime
import os

from .registry import register_tool

# Plugins 获取日期时间
@register_tool()
def get_time():
    """
    Получить текущую дату, время и день недели.
    
    Returns:
        Строка с текущей датой, временем и днем недели.
    """
    # Используем временную зону из переменной TZ или Киев по умолчанию
    timezone_name = os.getenv('TZ', 'Europe/Kiev')
    try:
        tz = pytz.timezone(timezone_name)
    except Exception:
        tz = pytz.timezone('Europe/Kiev')
        
    now = datetime.datetime.now(tz)
    weekday = now.weekday()
    
    # Дни недели на русском
    weekdays_ru = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    weekday_str = weekdays_ru[weekday]
    
    return f"Сегодня {now.date()}, время {now.strftime('%H:%M:%S')}, {weekday_str}."