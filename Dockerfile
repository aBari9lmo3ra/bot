# Задаем рабочую директорию внутри контейнера.
FROM python:3.11 

# Устанавливаем системные зависимости, необходимые для сборки некоторых Python-библиотек
WORKDIR /app

# Устанавливаем зависимости для сборки aiohttp
RUN apt-get update && apt-get install -y gcc python3-dev build-essential

#Устанавливаем все Python-зависимости, указанные в requirements.txt.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы проекта (включая bot.py и другие модули) в контейнер.
COPY . .

# Определяем команду, которая будет выполняться при запуске контейнера.
CMD ["python", "bot.py"]
