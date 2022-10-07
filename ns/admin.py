from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from ns.models import My_image  # импортируем модели из модельс

admin.site.register(My_image)  # зарегистрируем импортированные модели в админке
