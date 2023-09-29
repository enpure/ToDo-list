from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Пользователь, который создал задачу
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Заголовок задачи
    title = models.CharField(max_length=200)
    # Описание задачи
    description = models.TextField(null=True, blank=True)
    # Приоритет задачи
    priority = models.IntegerField(default=1)
    # Дата и время выполнения
    due_date = models.DateTimeField(null=True, blank=True)
    # Дата создания задачи
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
