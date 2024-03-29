from django import forms

class student(forms.Form):
    name = forms.CharField(max_length = 10,initial='XYZ')
    bio = forms.CharField(widget=forms.Textarea)
    address= forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(required = False,)
    BIRTH = ['1990', '1991', '1992', '1993', '1994', '1995','1996','1997', '1998','1999','2000']
    birth_Date = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH))
    subject_CHOICES = [
    ('1', 'CSE 102'),
    ('2', 'CSE 201'),
    ('3', 'DS 402'),
    ('4', 'EDA 202'),
    ('5', 'DBMS 402'),
    ('6', 'DSA 209'),
    ]

    Subject = forms.ChoiceField(choices= subject_CHOICES)
    value = forms.DecimalField()
    a = forms.BooleanField(label='terms&condition')