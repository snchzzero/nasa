from django.contrib import admin
from filer.admin.fileadmin import FileAdmin
from ns.models import My_image, SortableMy_image  # импортируем модели из модельс
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableInlineAdminMixin


#admin.site.register(My_image)  # зарегистрируем импортированные модели в админке

class ChapterTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SortableMy_image
    fields = ['image']

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        return extra

@admin.register(My_image)
class SortableBookAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ChapterTabularInline]


admin.site.site_title = 'Django Nasa_Project'
admin.site.site_header = 'Django Nasa_Project'