from django.contrib import admin
from .models import Heading, TodoItem

# Register your models here.


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'heading', 'completed', 'created_at')
    list_filter = ('completed',)
    search_fields = ('description', 'heading__title')
