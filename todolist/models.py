#author = Isha Shrestha

from django.db import models

# Create your models here.


class Todolist(models.Model):
    todo = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo

    # Internal class

    class Meta:
        db_table = "todolist"
