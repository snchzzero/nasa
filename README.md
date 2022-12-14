# Верстка web страницы по макету в Figma, запуск web страницы в Django
<details>
  <summary>Применяемые технологии</summary>
 django, django-filer, django-admin-sortable2, bootstrap 5.2, slick slider, html, docker
</details>

<a name="начало"></a>
[Инструкция по запуску веб сервиса (через docker)](#Инструкция_по_запуску)

**1. Для верстки страницы по макету [Figma](https://www.figma.com/file/B1BUcjTtTlrxu9XkvK1r8e/%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5?node-id=0%3A1) используется [bootstrap 5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/);**

Screenshot №1

![Screenshot](pic0.jpg)

**2. Для запуска слайдера используется [slick slider](http://kenwheeler.github.io/slick/)  (см. Slider Syncing);**

**3. [slick slider](http://kenwheeler.github.io/slick/) заполняется через django [admin](http://127.0.0.1:8000/admin/);**

Screenshot №2

![Screenshot](pic8.png)

**4. Для картинок модели слайдера добавлен новый пакет [django-filer](https://django-filer.readthedocs.io/en/latest/index.html) и через него загружаются картинки в слайдер;**

Screenshot №3

![Screenshot](pic4.JPG)

Screenshot №4

![Screenshot](pic5.JPG)

Screenshot №5

![Screenshot](pic6.JPG)

Screenshot №6

![Screenshot](pic7.JPG)

**5. Записи слайдера в админке сортируются при помощи drag&drop, для этого используется пакет [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/en/latest/index.html);**

Screenshot №7

![Screenshot](pic1.JPG)  

Screenshot №8

![Screenshot](pic2.JPG)

Screenshot №9

![Screenshot](pic3.JPG)

<a name="Инструкция_по_запуску">**Инструкция по запуску веб сервиса**</a>
1. перейти в папку \nasa и в терминале ввести следующие команды:
```shell
docker-compose build
docker-compose up   
```
2. для просмотра web страницы, в окне браузера перейти по адресу: http://127.0.0.1:8000/promo/


3. для доступа в панель администратора django, перейти по адресу: http://127.0.0.1:8000/admin/
```shell
Username: snchz
Password: djangodjango
```
[в начало](#начало)



 