from django import forms
from todo.models import TaskFieldModel

class TaskFieldForm(forms.ModelForm):
    class Meta:
        model = TaskFieldModel
        fields = '__all__'