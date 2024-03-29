from django.shortcuts import render
from .forms import student

# Create your views here.
def home(request):
    form=student()
    return render(request,'home.html',{'form':form})
