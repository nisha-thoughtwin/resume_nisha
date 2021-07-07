from django.urls import path
from . import views

#from .views import FresherResumeInput,ExperienceResumeInput,GenratePdf
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('home',Home.as_view(),name='home'),
    path("",sign_in,name="sign_in"),
    path("sign_up/",sign_up,name="sign_up"),
    # path('pdf/', GeneratePdf.as_view()), 
    
    path('',Home.as_view(),name='home'),
    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('fresher',FresherResumeInput.as_view(),name='fresher_input'),
    path('experience',ExperienceResumeInput.as_view(),name='experience_input'),

    path('generate',GenratePdf.as_view(),name='generate_pdf'),
    path('resume1/',Template1.as_view(),name='resume1'),
    path('resume2/',Template2.as_view(),name='resume2'),
    path('resume3/',Template3.as_view(),name='resume3'),

    path('resume4/',Template4.as_view(),name='resume4'),

    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('resume',Template5.as_view(),name='Template5'),
    # path('mail',views.mail,name='mail'),  
    
    path('logout', logout_request, name='logout'),

    path('updatedata/<int:id>/', views.UpdateFresherData.as_view(), name='updatedata'),
    path('update-edu/', views.UpdateEducation.as_view(), name='update_edu'),

 


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)