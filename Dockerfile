FROM yym68686/chatgpt:latest

# Отключаем интерактивные запросы
ENV DEBIAN_FRONTEND=noninteractive

# Копируем всё в корень
COPY . .

# Устанавливаем зависимости с принудительным обновлением
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Устанавливаем PYTHONPATH
ENV PYTHONPATH=$PYTHONPATH:.

# Явно указываем порт для Flask (Render его сам подставит, но так надежнее)
ENV PORT=10000

# Запускаем бота
CMD ["python", "bot.py"]