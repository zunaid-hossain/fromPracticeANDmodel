from django.shortcuts import render

from .forms import StudentForm
# Create your views here.


    
    
def home(request):
    if request.method =='POST':
        std = StudentForm(request.POST)
        if std.is_valid():
            std.save()
            print(std.changed_data)
    
    else:
        std = StudentForm()

    return render(request,'home.html',{'form':std})