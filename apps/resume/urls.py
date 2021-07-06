from django.urls import path
#from .views import FresherResumeInput,ExperienceResumeInput,GenratePdf
from django.conf import settings
from django.conf.urls.static import static
from .views import *
    
urlpatterns =[
    path('home',Home.as_view(),name='home'),
    path("",sign_in,name="sign_in"),
    path("sign_up/",sign_up,name="sign_up"),
    # path('pdf/', GeneratePdf.as_view()), 
    
    path('fresher',FresherResumeInput.as_view(),name='fresher_input'),
    path('experience',ExperienceResumeInput.as_view(),name='experience_input'),

    path('generate',GenratePdf.as_view(),name='generate_pdf'),
    path('resume1/',Template1.as_view(),name='resume1'),
    path('resume2/',Template2.as_view(),name='resume2'),
    path('resume3/<int:pk>',Template3.as_view(),name='resume3'),
    path('generate/pdf/', generate_pdf, name='generate_pdf'),


]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)