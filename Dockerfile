FROM yym68686/chatgpt:latest

# Отключаем интерактивные запросы
ENV DEBIAN_FRONTEND=noninteractive

# Принудительно устанавливаем часовой пояс Киева на уровне системы
ENV TZ=Europe/Kyiv
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Копируем всё в корень
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Устанавливаем PYTHONPATH
ENV PYTHONPATH=$PYTHONPATH:.

# Явно указываем порт
ENV PORT=10000

# Запускаем бота
CMD ["python", "bot.py"]