import datetime
from .registry import register_tool
from utils import globals

@register_tool()
async def set_reminder(minutes: int, text: str, convo_id: str = None):
    """
    Установить напоминание через определенное количество минут.
    
    Args:
        minutes: Через сколько минут отправить напоминание.
        text: Текст напоминания.
        convo_id: Идентификатор чата (заполняется автоматически).
    """
    if not globals.scheduler or not globals.bot:
        return "Ошибка: Планировщик не запущен."

    # Если convo_id не передан явно, это может быть проблемой, 
    # но мы подправим обработчик инструментов, чтобы он его прокидывал.
    if not convo_id:
        return "Ошибка: Не удалось определить ID чата."

    run_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    
    # Разбираем convo_id (он может быть в формате chatid_threadid)
    chat_parts = convo_id.split('_')
    chat_id = chat_parts[0]
    message_thread_id = chat_parts[1] if len(chat_parts) > 1 else None

    async def send_reminder():
        try:
            await globals.bot.send_message(
                chat_id=chat_id,
                text=f"🔔 Напоминание: {text}",
                message_thread_id=message_thread_id
            )
        except Exception as e:
            print(f"Ошибка при отправке напоминания: {e}")

    # Добавляем задачу в планировщик
    globals.scheduler.add_job(send_reminder, 'date', run_time=run_time)
    
    return f"Ок! Я напомню вам об этом через {minutes} мин. ({run_time.strftime('%H:%M:%S')})"
