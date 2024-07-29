import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set_permissions', blank=True)


class Tasks(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    """ чтобы сделать id типа uuid можно использовать строку ниже,
    но тогда будет затрудняться работа с методами, где используется id,
    поэтому сделал через другое поле, где сохраняется уникальность"""
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
