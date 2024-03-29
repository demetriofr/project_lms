## Платформа для онлайн-обучения

В мире развивается тренд на онлайн-обучение. Поэтому для веб-разработчика важно не только обучиться, но и знать, 
как реализовать платформу для онлайн-обучения. 

**Цель проекта:** Разработка LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.

Данный проект это SPA веб-приложение и результатом создания его будет бэкенд-сервер, который возвращает клиенту 
JSON-структуры.


### ДЗ: 24.1 Вьюсеты и дженерики

#### Задание 1
- [x] Создайте новый Django-проект, подключите DRF в настройках проекта.

#### Задание 2
Создайте следующие модели:

- [x] Пользователь:
все поля от обычного пользователя, но авторизацию заменить на email; 
- телефон; 
- город; 
- аватарка.
- [x] Модель пользователя разместите в приложении users

- [x] Курс:
- название, 
- превью (картинка), 
- описание.

- [x] Урок:
- название, 
- описание, 
- превью (картинка), 
- ссылка на видео.

**Урок и курс** - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков. 
- [x] Реализуйте связь между ними.

- [x] Модель курса и урока разместите в отдельном приложении. 
Название для приложения выбирайте такое, чтобы оно описывало то, с какими сущностями приложение работает. Например, 
lms или materials - отличные варианты.


#### Задание 3
- [x] Опишите CRUD для моделей курса и урока. 
Для реализации CRUD
- - [x] для курса используйте Viewsets, 
- - [x] а для урока - Generic-классы.

- [x] Для работы контроллеров опишите простейшие сериализаторы.

- [x] При реализации CRUD для уроков реализуйте все необходимые операции (получение списка, получение одной сущности, 
создание, изменение и удаление).

- [x] Работу каждого эндпоинта необходимо проверять с помощью Postman.

Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже 
самой простой авторизацией.


#### Дополнительное задание
- [x] Реализуйте эндпоинт для редактирования профиля любого пользователя на основе более привлекательного подхода для 
личного использования: Viewset или Generic.
