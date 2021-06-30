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

res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 8))
random_password = str(res)
def userdate(dt_time):
    return str(10000*dt_time.year+100*dt_time.month+dt_time.day)


def usernameGen(names):
    names = names.split(" ") 
    for i in range(1,1000):
        first_letter = names[0][0]
        three_letter = names[-1][:3]
        number = '{:03d}'.format(random.randrange(1,1000))
        dateuser = userdate(date.today())
        username =(first_letter+three_letter+dateuser+number)

        try:
            User.objects.get(username = username)
            return usernameGen("PMK GAC")
        except User.DoesNotExist:
            return username

class Home(View):

    def get(self, request):
        return render(request, 'index.html')


class FresherResumeInput(View):

    def get(self, request):

        form1 = ResumeForm
        form2 = UserExtraFieldsForm
        form3 = EducationForm
        form4 = SkillsForm
        form5 = ExperienceForm
        form6 = HobbiesForm
        form7 = CertificateForm
        form8 = AchievementsForm
        context = {'form1': form1, 'form2': form2,
                   'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8}

        return render(request, 'resume/fresher.html', context)

    def post(self, request):
        form1 = ResumeForm(request.POST)
        user = User.objects.create(username=usernameGen("PMK GAC"),password=random_password)

        form2 = UserExtraFieldsForm(request.POST)
        
        form3 = EducationForm(request.POST)
        form4 = SkillsForm(request.POST)
        form6 = HobbiesForm(request.POST)
        form7 = CertificateForm(request.POST)
        form8 = AchievementsForm(request.POST)
        if form1.is_valid and form2.is_valid and form3.is_valid and form4.is_valid and form6.is_valid and form7.is_valid and form8.is_valid:
            form1.save()
            form2.save()
            form3.save()
            form4.save()
            form6.save()
            form7.save()
            form8.save()

            return HttpResponse("done")
        return HttpResponse("not done")




class ExperienceResumeInput(View):

    def get(self, request):
        form1 = ResumeForm
        form2 = UserExtraFieldsForm
        form3 = EducationForm
        form4 = SkillsForm
        form5 = ExperienceForm
        form6 = HobbiesForm
        form7 = CertificateForm
        form8 = AchievementsForm
        context = {'form1': form1, 'form2': form2,
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
        return render(request,'resume/template2.html')

    
