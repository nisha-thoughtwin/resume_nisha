from django.urls import path
from . import views

#from .views import FresherResumeInput,ExperienceResumeInput,GenratePdf
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .choice import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',Home.as_view(),name='home'),
    path("login",sign_in,name="sign_in"),
    path("sign_up/",sign_up,name="sign_up"),
    # path('pdf/', GeneratePdf.as_view()), 
    

    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('fresher',FresherResumeInput.as_view(),name='fresher_input'),
    path('experience',ExperienceResumeInput.as_view(),name='experience_input'),

    # path('generate',GenratePdf.as_view(),name='generate_pdf'),
    path('resume1/',Template1.as_view(),name='resume1'),
    path('resume2/',Template2.as_view(),name='resume2'),
    path('resume3/',Template3.as_view(),name='resume3'),

    path('resume4/',Template4.as_view(),name='resume4'),

    path('dashboard',Dashboard.as_view(),name='dashboard'),
    path('resume',Template5.as_view(),name='Template5'),
    # path('mail',views.mail,name='mail'),  
    
    path('logout', logout_request, name='logout'),
    # path('generate_pdf/pdf',generate_pdf,name='generate_pdf'),

     path('updateresume/<int:id>/', views.ViewResumeDetail.as_view(), name='updateresume'),
   
   
    path('add-edu/', views.AddEducation.as_view(), name='add_education'),
    path('update-edu/', views.UpdateEducation.as_view(), name='update_edu'),
    path('deleteEdu/', views.DeleteEducation.as_view(), name='deleteEdu'),

    path('add-skills/', views.AddSkillsData.as_view(), name='add_skills'),
    path('deleteskill/<int:id>/', views.DeleteSkills.as_view(), name='deleteskill'),
    path('update_skill/',UpdateSkills.as_view(),name='update_skill'),

    path('add-hobbie/', views.AddHobbiesData.as_view(), name='add_hobbies'),
    path('deletehobbie/<int:id>/', views.DeleteHobbies.as_view(), name='deletehobbie'),
    path('update_hobbie/',UpdateHobbies.as_view(),name='update_hobbie'),


    path('add-achievements/', views.AddAchievementsData.as_view(), name='add_achievements'),
    path('deleteachievements/<int:id>/', views.DeleteAchievements.as_view(), name='deleteachievements'),
    path('update_achievements/',UpdateAchievements.as_view(),name='update_achievements'),


    path('add-experience/', views.AddExperienceData.as_view(), name='add_experience'),
    path('deleteexperience/', views.DeleteExperience.as_view(), name='deleteexperience'),
    path('update_experience/',UpdateExperience.as_view(),name='update_experience'),

    path('template1', choose_template1, name='template1'),
    path('template2', choose_template2, name='template2'),
    path('template3', choose_template3, name='template3'),
    path('template4', choose_template4, name='template4'),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)