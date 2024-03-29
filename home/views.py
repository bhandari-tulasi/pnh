from django.shortcuts import render, get_object_or_404, redirect
from . models import Department, Doctor, Staff

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
    staffs = Staff.objects.all()
    # hib_staffs = Staff.objects.get(name__case_exact=department)
    
    context = {
        'staffs':staffs,
        # 'hib_staffs':hib_staffs,
    }
    return render(request, 'staffs.html', context)

def vacancy(request):
    
    return render(request, 'vacancy.html')


def deleteDoctor(request, id):
    # Retrieve the doctor object or return 404 if not found
    doctor = get_object_or_404(Doctor, id=id)
    
    if request.method == "POST":
        # If the request method is POST, it means the user has confirmed deletion
        doctor.delete()
        # Redirect to a success URL after deletion, you can customize this URL
        return redirect('/')
    
    # Render a template or return a response indicating confirmation of deletion
    # Here you can render a confirmation page or handle deletion confirmation in some other way
    return render(request, 'confirmation_template.html', {'doctor': doctor})
