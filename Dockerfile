FROM yym68686/chatgpt:latest

# Копируем всё в корень, как в оригинальном образе
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем переменную окружения, чтобы Python видел все папки
ENV PYTHONPATH=$PYTHONPATH:.

# Запускаем бота
CMD ["python", "bot.py"]