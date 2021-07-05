from django.urls import path
from . import views

#from .views import FresherResumeInput,ExperienceResumeInput,GenratePdf
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('fresher',FresherResumeInput.as_view(),name='fresher_input'),
    path('experience',ExperienceResumeInput.as_view(),name='experience_input'),

    path('generate',GenratePdf.as_view(),name='generate_pdf'),

    path('resume2/',Template2.as_view(),name='resume2'),
    path('resume3/',Template3.as_view(),name='resume3'),

    path('resume4/',Template4.as_view(),name='resume4'),

    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('resume',Template5.as_view(),name='Template5'),##poornima
    path('mail',views.mail,name='mail')  





]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)