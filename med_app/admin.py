from django.contrib import admin
from .models import Doctors, Appointment, ContactUs

# Register your models here.

admin.site.register(Doctors)
admin.site.register(Appointment)
admin.site.register(ContactUs)