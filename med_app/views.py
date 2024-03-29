from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctors, Appointment, ContactUs

from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse

# for emailsending
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def index(request):
    # if you want to display the docotrs list from the database use the following
    doc = Doctors.objects.all()

    # to display unique values of speciality
    # specialities = Doctors.objects.values_list('speciality', flat=True).distinct()
    return render(request, 'index.html', {'doctors': doc})

def doctors(request):
    doc = Doctors.objects.all()      
    return render(request, 'doctors.html', {'doctor': doc})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        enquiry = ContactUs(
            name=name, 
            email=email,
            phone=phone,
            message=message
        )
        enquiry.save()

        messages.success(request, "We have recieved your message, we will getback to you asap!")
        return redirect('index')
        
    else:
        return render(request, 'contact.html')


def book_appointment(request):
    if request.method == 'POST':
        try:
            name = request.POST['pt_name']
            email = request.POST['email']
            phone = request.POST['phone']
            department = request.POST['department']
            doctor = request.POST['doctor']
            date_str = request.POST['date']
            # Parse the date string and convert it to the 'YYYY-MM-DD' format (required date format for postgresql)
            date = datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
            message = request.POST['message']

            # Create the Appointment object and save it
            apptm = Appointment.objects.create(
                pt_name=name,
                email=email,
                phone=phone,
                department=department,
                doctor=doctor,
                date=date,
                message=message
            )

            messages.success(request, 'Appointment booked successfully!')

            # Redirect after successful form submission to avoid form resubmission on page refresh
            return redirect('index')
        except MultiValueDictKeyError as e:
            return HttpResponseBadRequest("Missing key in form submission: {}".format(e))
        except ValueError:
            return HttpResponseBadRequest("Invalid date format. Date must be in MM/DD/YYYY format.")
    else:
        return render(request, 'index.html')


def about(request):
    return render(request, 'about.html', {'request': request})

def blog(request):
    return render(request, 'blog.html', {'request': request})

def portfolio(request):
    return render(request, 'portfolio.html', {'request': request})

def specialities(request):
    return render(request, 'specialities.html', {'request': request})

# searching doctors by name/speciality
def search(request):
    if request.method == 'POST':

        doc_query = request.POST.get('doctor')
        spec_query = request.POST.get('spec')
        doctors_query = Doctors.objects.all()
    
        if doc_query:
            doctors_query = doctors_query.filter(name__icontains=doc_query)
        if spec_query:
            doctors_query = doctors_query.filter(speciality__icontains=spec_query)
        
        return render(request, 'search.html', {'doctor':doctors_query})
    
    return render(request, 'search.html')

