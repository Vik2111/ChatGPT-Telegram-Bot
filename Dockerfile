FROM yym68686/chatgpt:latest

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы из текущей папки в образ
COPY . .

# Устанавливаем зависимости из нашего requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду для запуска именно нашего бота
CMD ["python", "bot.py"]