# import form class from django
from django import forms

# import Todolist from models.py
from .models import Todolist

# create a ModelForm 
class TodoForm(forms.ModelForm):
     #name of model is specified
     class Meta:
        model = Todolist
        fields = ['id','todo']
