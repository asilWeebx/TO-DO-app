from django import forms
from main.models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo()
        fields = '__all__'
