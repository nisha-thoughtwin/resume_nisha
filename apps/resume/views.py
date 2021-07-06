from collections import UserString
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import UserForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
import pdfkit
from .models import *
from .forms import *
import random
from datetime import date
import string
from django.contrib.auth.models import User
date = date.strftime
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#importing get_template from loader
from django.template.loader import get_template
 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 



def sign_up(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(username=username,email=email,password=password)
            return render(request,"resume/sign_up.html",{"status":"Mr/Miss. {} your Account created Successfully".format(username)})
        except IntegrityError as e:
            return render(request,"resume/sign_up.html", {"status":"Mr/Miss. {} your Account Already  Exist".format(username)})
    return render(request,"resume/sign_up.html")



def sign_in(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'resume/sign_in.html')

@method_decorator(login_required,name='dispatch')
class Home(View):
    def get(self, request):
        return render(request, 'index.html')

@method_decorator(login_required,name='dispatch')
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
            eductation.user = user
            eductation.save()
            skills = form4.save(commit=False)
            skills.resume = resume
            skills.user = user
            skills.save()
            hobbies = form5.save(commit=False)
            hobbies.resume = resume
            hobbies.user = user
            hobbies.save()
            certificate = form6.save(commit=False)
            certificate.resume = resume
            certificate.user = user
            certificate.save()
            achievements = form7.save(commit=False)
            achievements.resume = resume
            achievements.user = user
            achievements.save()
            return HttpResponse("done")
        return HttpResponse("not done")
    
@method_decorator(login_required,name='dispatch')
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
    
@method_decorator(login_required,name='dispatch')
class GenratePdf(View):
    def post(self, request):
        if request.method == 'POST':
            url = request.POST.get('temp_url')
            pdf = pdfkit.from_url(url, 'file1.pdf')
            # resume = Resume.objects.create(resume=pdf)
            return HttpResponse('download success')


@method_decorator(login_required,name='dispatch')
class Template2(View):
    def get(self, request):
        context ={}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume']= resume
        # print(resume.education_set.all().first().degree_class)    
        # print(resume._set.all().first().phone)  
        # for i in resume.education_set.all():
        #    print(i.degree_class)
        return render(request,'resume/template2.html', context)

@method_decorator(login_required,name='dispatch')
class Template3(View):
    def get(self,request):
        context={}
        user_extra_filed=UserExtraFields.objects.get(user__pk=4)
        education=Education.objects.get(user__pk=4)
        experience=Experience.objects.get(user__pk=4)
        skills=Skills.objects.get(user__pk=4)
        hobbies=Hobbies.objects.get(user__pk=4)
        certification=Certificate.objects.get(user__pk=4)
        achievements=Achievements.objects.get(user__pk=4)
        context['user_extra_filed']=user_extra_filed
        context['education']=education
        context['experience']=experience
        context['skills']=skills
        context['hobbies']=hobbies
        context['certification']=certification
        context['achievements']=achievements
        return render(request,'resume/template3.html',context=context)


  # ---------------------------

# #importing get_template from loader
# from django.template.loader import get_template
 
# #import render_to_pdf from util.py 
# from .utils import render_to_pdf 
 
# #Creating our view, it is a class based view
# class GeneratePdf(View):
#      def get(self, request, *args, **kwargs):
        
#         #getting the template
#         pdf = render_to_pdf('resume/template2.html')
         
#          #rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')        


#------------------------------

# -*- coding: utf-8 -*-
# from .models import Person
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


# def generate_pdf(request):
#     """Generate pdf."""
#     # Model data
#     # people = Person.objects.all().order_by('last_name')
#     context ={}
#     user = request.user
#     resume = Resume.objects.get(user=user)
#     context['resume']= resume
#     print(resume.education_set.all()) 
#     # Rendered
#     html_string = render_to_string('resume/template2.html',context)
#     html = HTML(string=html_string)
#     result = html.write_pdf()

#     # Creating http response
#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=list_people.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'rb')
#         response.write(output.read())

#     return response

#----------------------------------------------------------------
# install Pdfcrowd: "pip install pdfcrowd", more...

import sys
import logging
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django import forms
import pdfcrowd
import logging



def generate_pdf(request):
    # form = TestForm(request.POST)
    if request.method != 'POST':
        return render(request, 'resume/template2.html')

    try:
        # enter your Pdfcrowd credentials to the converter's constructor
        client = pdfcrowd.HtmlToPdfClient('resume', 'ce544b6ea52a5621fb9d55f8b542d14d')

        part = request.POST.get('part_for_conversion')
        if part != None and part != 'all':
            # convert just selected part of the page
            client.setElementToConvert(part)

        # convert a web page and store the generated PDF to a variable
        logger.info('running Pdfcrowd HTML to PDF conversion')

        # set HTTP response headers
        response = HttpResponse(content_type='application/pdf')
        response['Cache-Control'] = 'max-age=0'
        response['Accept-Ranges'] = 'none'
        content_disp = 'attachment' if 'asAttachment' in request.POST else 'inline'
        response['Content-Disposition'] = content_disp + '; filename=demo_django.pdf'

        html = render_to_string(
            'resume/template2.html', {
                'form': form,
                'pdfcrowd_remove': 'pdfcrowd-remove' if form.data.get('remove_convert_button') else ''
                })
        client.convertStringToStream(html, response)

        # send the generated PDF
        return response
    except pdfcrowd.Error as why:
        logger.error('Pdfcrowd Error: %s', why)
        return HttpResponse(why)
