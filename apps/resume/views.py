
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from resume_maker.settings import MAIL
from django.core import mail
from django.http import HttpResponse  
from resume_maker import settings  
from django.core.mail import send_mail  
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

from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 



def sign_up(request):
    if request.method=="POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        password = request.POST["password"]
        # email = request.POST["email"]
        try:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
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
            return redirect('dashboard')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'resume/sign_in.html')
  

def mail(user,password):  
    subject = "Greetings"  
    msg     = f"Congratulations for your successfull ResumeForm username {user} ,passowrd {password}"  
    to      = "nisha.thoughtwin@gmail.com"  
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not sent"  
    return HttpResponse(msg)  


class Home(View):
    def get(self, request):
        return render(request, 'index.html')

class Dashboard(View):
    @method_decorator(login_required)
    def get(self, request):
        # import pdb
        # pdb.set_trace()
        user = request.user
        resume = Resume.objects.filter(user = user)
        return render(request, 'resume/dashboard.html', {'resume': resume, })        

@method_decorator(login_required,name='dispatch')
class FresherResumeInput(View):
    def get(self, request):
        form = ResumeForm
        form1 = UserForm
        form2 = UserExtraFieldsForm
        form3 = EducationFormSet(queryset=Education.objects.none())
        form4 = SkillsFormSet(queryset=Skills.objects.none())

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

        form3 = EducationFormSet(data=request.POST)
        # print(form3)

        form4 = SkillsFormSet(request.POST,None)
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
            user.set_password(random_password)

            user.save()
            resume = form.save(commit=False)
            resume.user = user
            resume.save()

            userextra = form2.save(commit=False)
            userextra.resume = resume
            # userextra.user = user

            userextra.save()
            for f in form3:
                # print(f)

                eductation = f.save(commit=False)
                eductation.resume = resume
                eductation.save()

            
            for s in form4: 
           
                skills = s.save(commit=False)
                skills.resume = resume
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

            username = username
            raw_password = random_password
            user = authenticate(username=username, password=raw_password)

            # mail(username,random_password)


            login(request, user)
            return redirect('dashboard')


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
# class GenratePdf(View):
#     def post(self, request):
#         if request.method == 'POST':
#             url = request.POST.get('temp_url')
#             pdf = pdfkit.from_url(url, 'file1.pdf')
#             # resume = Resume.objects.create(resume=pdf)
#             return HttpResponse('download success')

@method_decorator(login_required,name='dispatch')
class Template1(View):
    def get(self, request):
        context ={}
        user = request.user
        # print(user)
        resume = Resume.objects.get(user=user)
        context['resume']= resume
        # print(resume.education_set.all().first().degree_class)
        #mail(resume)
        return render(request,'resume/template1.html', context)


@method_decorator(login_required,name='dispatch')
class Template2(View):
    def get(self, request):
        return render(request, 'resume/template2.html')


def logout_request(request):
	logout(request)
	return redirect("/")

# class Template3(View):
#     def get(self,request):
#         context={}
#         user_extra_filed=UserExtraFields.objects.get(user__pk=4)
#         education=Education.objects.get(user__pk=4)
#         experience=Experience.objects.get(user__pk=4)
#         skills=Skills.objects.get(user__pk=4)
#         certification=Certificate.objects.get(user__pk=4)
#         achievements=Achievements.objects.get(user__pk=4)
#         context['user_extra_filed']=user_extra_filed
#         context['education']=education
#         context['experience']=experience
#         context['skills']=skills
#         context['certification']=certification
#         context['achievements']=achievements
        
#         return render(request,'resume/template3.html',context=context)



# class Template4(View):
#     def get(self, request):
#         context = {}
#         user = request.user
#         resume = Resume.objects.get(user=user)
#         context['resume'] = resume
#         # print(resume.education_set.all().first().degree_class)
#         # for i in resume.education_set.all():
#         #    print(i.degree_class)


#         return render(request, 'resume/template4.html', context)

class Template3(View):
    def get(self, request):
        context = {}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume'] = resume
        # print(resume.education_set.all()) 

        # print(resume.education_set.all().first().degree_class)
        # for i in resume.education_set.all():
        #    print(i.degree_class)


        return render(request, 'resume/template3.html', context)


class Template4(View):
    def get(self, request):
        context = {}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume'] = resume
        # print(resume.education_set.all().first().degree_class)
        # for i in resume.education_set.all():
        #    print(i.degree_class)



        return render(request, 'resume/template4.html', context)
        
#         #getting the template
#         pdf = render_to_pdf('resume/template2.html')
         
#          #rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')        


#------------------------------

# -*- coding: utf-8 -*-

def generate_pdf(request):
    """Generate pdf."""
    # Model data
    # people = Person.objects.all().order_by('last_name')
    context ={}
    user = request.user
    resume = Resume.objects.get(user=user)
    context['resume']= resume
    print(resume.education_set.all()) 
    # Rendered
    html_string = render_to_string('resume/template1.html',context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=resume.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response


class UpdateFresherData(View):
    @method_decorator(login_required)
    def get(self, request, id):
        resume =  Resume.objects.get(pk=id)
        modeleducation = Education.objects.filter(pk=id).first()
        modelHobbies = Hobbies.objects.filter(pk=id ).first()
        modelSkills = Skills.objects.filter(pk=id).first()
        modelcertificate = Certificate.objects.filter(pk=id).first()
        modelachievements = Achievements.objects.filter(pk=id).first()
        form = EducationForm(instance=modeleducation)
        form1 = HobbiesForm(instance=modelHobbies)
        form2 = SkillsForm(instance=modelSkills)
        form3 = CertificateForm(instance=modelcertificate)
        form4 = AchievementsForm(instance=modelachievements)
        eduform = EducationForm()
        education = Education.objects.filter(resume=resume)
        context = {'form': form,'form1': form1,'form2': form2,'form3': form3,'form4': form4,
        'eduform':eduform,'education':education}
        return render(request, 'resume/updatedata.html',context)
    @method_decorator(login_required)
    def post(self, request, id):
        resume =  Resume.objects.get(pk=id)
        print(resume)
        addeduform = EducationForm(request.POST)
        modeleducation = Education.objects.get(pk=id)   
        # modelHobbies = Hobbies.objects.get(pk=id)
        # modelSkills = Skills.objects.get(pk=id)
        # modelcertificate = Certificate.objects.get(pk=id)
        # modelachievements = Achievements.objects.get(pk=id)
        form = EducationForm(request.POST ,instance=modeleducation)
        # form1 = HobbiesForm(request.POST ,instance=modelHobbies)
        # form2 = SkillsForm(request.POST ,instance=modelSkills)
        # form3 = CertificateForm(request.POST ,instance=modelcertificate)
        # form4 = AchievementsForm(request.POST ,instance=modelachievements)
        if addeduform.is_valid:
            addeduform.save(commit=False)
            addeduform.resume=resume
            addeduform.save()
            return redirect('dashboard')
        elif form.is_valid :
            form.save()
            # form2.save()
            # form3.save()
            # form4.save()
            return render(request, 'resume/updatedata.html')
        else:
            return HttpResponse("NOT VALID REQ")


#----------------------------------------------------------------
