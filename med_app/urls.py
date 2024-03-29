from django.urls import path
from med_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('doctors', views.doctors, name='doctors'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('book_appointment', views.book_appointment, name='appointment'),
    path('search', views.search, name='search'),
    path('specilities', views.specialities, name='specialities'),
]

