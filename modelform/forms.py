from django import forms
from .models import studentModel

class StudentForm(forms.ModelForm):
    
    class Meta:
        model = studentModel
        fields ='__all__' 
        labels={

            'name': 'Student name', 
            'Id': 'Student Id',
        }