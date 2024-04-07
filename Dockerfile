# Используем базовый образ Python
FROM python:3.12

# Устанавливаем переменную окружения для отключения вывода данных Python в буферизованный режим
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Выполняем миграции и собираем статические файлы Django приложения
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
