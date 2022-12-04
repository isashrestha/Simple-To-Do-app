#author = Isha Shrestha

#import the standard Django Model
#from built-in library
from django.db import models

# declaring a model with a name "Todolist"
class Todolist(models.Model):
    #fields of the model
    todo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

          #rename the instance of the model
          #with their title name
    def __str__(self):
        return self.todo

    # Internal class
    class Meta:
        db_table = "todolist"
