from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'index.html')


def management(request):

    return render(request, 'hm.html')


def about(request):
    
    return render(request, 'about.html')


def contact(request):
    
    return render(request, 'contact.html')

def doctors(request):
    
    return render(request, 'doctors.html')

def download(request):
    
    return render(request, 'download.html')

def news(request):
    
    return render(request, 'news.html')

def reporting(request):
    
    return render(request, 'reporting.html')

def services(request):
    
    return render(request, 'services.html')

def staff(request):
    
    return render(request, 'staffs.html')

def vacancy(request):
    
    return render(request, 'vacancy.html')


