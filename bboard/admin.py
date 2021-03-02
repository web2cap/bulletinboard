from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bb

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published','rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

#регистрация можеди в админке
admin.site.register(Bb, BbAdmin)

from .models import Rubric

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(Rubric, RubricAdmin)