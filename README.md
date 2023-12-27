# django_stripe

## Основной функционал

```
- Django Модель Item с полями (name, description, price)
- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy.
  По нажатию на кнопку Buy должен происходить запрос на /buy/{id},
  получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
```

## Бонусные задачи
```
- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
```

## Установка и запуск
```
1.python -m venv venv
2.Windows - .\venv\Scripts\activate / Linux - source venv/bin/activate
3.pip install -r requirements.txt
4.В корне проекта python manage.py migrate
5.python manage.py createsuperuser
6.python manage.py runserver
```

### Docker
```
- sudo docker build -t stripe .
- sudo docker run -p 8000:8000 stripe
```
