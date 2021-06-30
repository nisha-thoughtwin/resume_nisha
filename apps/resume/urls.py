from django.urls import path
#from .views import FresherResumeInput,ExperienceResumeInput,GenratePdf
from .views import *
    
urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('fresher',FresherResumeInput.as_view(),name='fresher_input'),
    path('experience',ExperienceResumeInput.as_view(),name='experience_input'),

    path('generate',GenratePdf.as_view(),name='generate_pdf'),

    path('resume2/',Template2.as_view(),name='resume2')
]