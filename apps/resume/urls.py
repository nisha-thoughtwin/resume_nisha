from django.urls import path
#from .views import FresherResumeInput,ExperienceResumeInput,GenratePdf
from .views import *
    
urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('fresher',FresherResumeInput.as_view(),name='fresher_input'),
    path('experience',ExperienceResumeInput.as_view(),name='experience_input'),

    path('generate',GenratePdf.as_view(),name='generate_pdf'),

    path('resume2/',Template2.as_view(),name='resume2'),
    path('resume4/',Template4.as_view(),name='resume4'),

    path('dashboard',Dashboard.as_view(),name='dashboard'),

    path('logout', logout_request, name='logout'),


]