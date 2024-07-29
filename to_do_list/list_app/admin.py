from django.contrib import admin
from list_app.models import User, Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения задач в админке.
    """

    list_display = ("id", "title", "user", "created_at", "updated_at")
    list_display_links = ("title", "user")
    ordering = ["title"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения пользователя в админке.
    """

    list_display = ("username", "email", "last_name", "first_name", )
    list_display_links = ("last_name", "first_name", "email", )
    ordering = ["username"]
