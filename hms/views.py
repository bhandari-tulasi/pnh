from django.shortcuts import render
from .forms import *
# Create your views here.
def dashboard(request):
    
    # form = DepartmentForm()

    # if request.method =='POST':
    #     #print(request.POST)
    #     form = DepartmentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
            
    # context = {'form':form}
    return render(request, 'dashboard.html')


def addDepartment(request):
    form = DepartmentForm

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {
        'form':form
    }
    
    return render(request, 'addDepartment.html', context)

def addDoctor(request):
    form = DoctorForm()

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form':form
    }   

    return render(request, 'addDoctor.html', context)     
