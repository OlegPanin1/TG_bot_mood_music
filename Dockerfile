FROM python:3.9-slim

# Указываем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной проект
COPY . .

# Команда, которую надо запустить
CMD ["python", "app/bot.py"]
