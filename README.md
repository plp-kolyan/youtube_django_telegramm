# **django python - проостой телеграмм бот**
Это пример простого телеграмм бота на python который отвечат на зарание указанные сообщения пользователя

# Установка
1. Сделайте клон текущего репозитория
2. Установите зависимости
   `pip install -r requirements.txt`
3. Создайте serveses_config.py в корне проекта с содержимым

    bot_token = '********************************'

    api_id = ******

    api_hash = '********************'
4. Выполните `python manage.py makemigrations`
5. Выполните `python manage.py migrate`
6. Создайте Юзера `python manage.py createsuperuser`
7. Запустите сервер `python manage.py runserver`
8. Запустите бота `python manage.py start_bot`
9. Зайдите в админку http://127.0.0.1:8000/admin/simplebot/answer - в поле Command пишите текст пользователя, в Text сообщение бота


##### **Смотрите другие видео о python django telegramm на канале**

https://www.youtube.com/@djangoadvice

##### **Платные консультации python django telegramm bot**

https://t.me/djangoadvice

