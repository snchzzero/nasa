# Верстка web страницы по макету в Figma, запуск web страницы в Django
<details>
  <summary>Применяемые технологии</summary>
 django, django-filer, django-admin-sortable2, bootstrap 5.2, slick slider, html, docker
</details>

**1. Для верстки страницы используется [bootstrap 5.2](https://getbootstrap.com/docs/5.2/getting-started/introduction/);**

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



 