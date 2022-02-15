from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group



class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-' 

class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('title', 'slug')
    list_editable = ('slug',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('slug',)
    empty_value_display = '-пусто-'  



# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)

admin.site.register(Group,GroupAdmin)