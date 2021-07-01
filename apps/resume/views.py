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


date = date.strftime


class Home(View):

    def get(self, request):
        return render(request, 'index.html')


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

        form = ResumeForm(request.POST)
        form1 = UserForm(request.POST)

        form2 = UserExtraFieldsForm(request.POST, request.FILES)

        form3 = EducationForm(request.POST)
        form4 = SkillsForm(request.POST)
        form5 = HobbiesForm(request.POST)
        form6 = CertificateForm(request.POST)
        form7 = AchievementsForm(request.POST)

        if form.is_valid and form1.is_valid and form2.is_valid and form3.is_valid and form4.is_valid and form5.is_valid and form6.is_valid and form7.is_valid:

            resume = form.save()
            user = form1.save(commit=False)
            username = first_name+str(random.randrange(100, 1000))
            if username not in User.objects.all():
                user.username = username
            user.password = random_password

            user.save()

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

            return HttpResponse("done")
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
