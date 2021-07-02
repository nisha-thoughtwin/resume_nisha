from collections import UserString
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
import pdfkit
from .models import *
from .forms import *
#from .models import Resume, Education,skills,experience,hobbies,certifications,acheivments
#from .forms import Resume, Education,skills,experience,hobbies,certifications,acheivments

import random
from datetime import date
import string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
<<<<<<< HEAD

=======
>>>>>>> 8e8a3643b2297465c0388c15fe013db41f69f0dc

date = date.strftime


class Home(View):

    def get(self, request):
        return render(request, 'index.html')

class Dashboard(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


class Dashboard(View):
    
   
    def get(self, request):

        return render(request, 'resume/dashboard.html')

class FresherResumeInput(View):

    def get(self, request):

        form = ResumeForm
        form1 = UserForm
        form2 = UserExtraFieldsForm
        form3 = EducationForm
        form4 = SkillsForm

        form5 = HobbiesForm
        form6 = CertificateForm
        form7 = AchievementsForm
        
        context = {'form': form, 'form1': form1, 'form2': form2,
                   'form3': form3, 'form4': form4, 'form5': form5, 'form7': form7, 'form6': form6}

        return render(request, 'resume/fresher.html', context)

    def post(self, request):
        print(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        res = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=8))
        random_password = str(res)
        print(random_password)
        # D70LOX2Y

        form = ResumeForm(request.POST)
        form1 = UserForm(request.POST)

        form2 = UserExtraFieldsForm(request.POST, request.FILES)

        form3 = EducationForm(request.POST)
        

        form4 = SkillsForm(request.POST)
        form5 = HobbiesForm(request.POST)
        form6 = CertificateForm(request.POST)
        form7 = AchievementsForm(request.POST)

        # user_data = User.objects.all(request.user)

        if form.is_valid and form1.is_valid and form2.is_valid and form3.is_valid and form4.is_valid and form5.is_valid and form6.is_valid and form7.is_valid:

            
            
            
            # for degree in request.POST.getlist('degree_class'):
            #     e=Education(degree_class=degree)
                
            #     e.resume= resume
            #     for year in request.POST.getlist('year_of_passing'):
            #         e.year_of_passing=year
                
            #     for percentage in request.POST.getlist('percentage_or_grade',):
            #         e.percentage_or_grade=percentage
            #     for college in request.POST.getlist('university'):
            #         e.university= college

            #     e.save()

            
           
            user = form1.save(commit=False)
            username = first_name+str(random.randrange(100, 1000))
            if username not in User.objects.all():
                user.username = username
<<<<<<< HEAD
                user.set_password(random_password)
=======
            user.set_password(random_password)
>>>>>>> 8e8a3643b2297465c0388c15fe013db41f69f0dc

            user.save()
            resume = form.save(commit=False)
            resume.user = user

            userextra = form2.save(commit=False)
            userextra.resume = resume
            userextra.user = user

            userextra.save()
            eductation = form3.save(commit=False)
            eductation.resume = resume
            eductation.save()
            skills = form4.save(commit=False)
            skills.resume = resume
            skills.save()
            hobbies = form5.save(commit=False)
            hobbies.resume = resume
            hobbies.save()
            certificate = form6.save(commit=False)
            certificate.resume = resume
            certificate.save()
            achievements = form7.save(commit=False)
            achievements.resume = resume
            achievements.save()

<<<<<<< HEAD
            username = username
            raw_password = random_password
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')

=======
            
            user = authenticate(username=username, password=random_password)
            login(request, user)
            return redirect('dashboard')
          
>>>>>>> 8e8a3643b2297465c0388c15fe013db41f69f0dc
        return HttpResponse("not done")


class ExperienceResumeInput(View):

    def get(self, request):
        form = ResumeForm
        form1 = UserForm
        form2 = UserExtraFieldsForm
        form3 = EducationForm
        form4 = SkillsForm
        form5 = ExperienceForm
        form6 = HobbiesForm
        form7 = CertificateForm
        form8 = AchievementsForm
        context = {'form': form, 'form1': form1, 'form2': form2,
                   'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8}

        return render(request, 'resume/experience.html', context)


class GenratePdf(View):

    def post(self, request):

        if request.method == 'POST':
            url = request.POST.get('temp_url')
            pdf = pdfkit.from_url(url, 'file1.pdf')
            # resume = Resume.objects.create(resume=pdf)
            return HttpResponse('download success')


class Template2(View):
    def get(self, request):
        return render(request, 'resume/template2.html')

<<<<<<< HEAD

def logout_request(request):
	logout(request)
	return redirect("/")
=======
class Template4(View):
    def get(self, request):
        context ={}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume']= resume
        print(resume.education_set.all().first().degree_class) 
        # for i in resume.education_set.all():
        #    print(i.degree_class)

        return render(request,'resume/template4.html', context)
>>>>>>> 8e8a3643b2297465c0388c15fe013db41f69f0dc
