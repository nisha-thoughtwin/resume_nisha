from .utils import render_to_pdf
from django.core import mail
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.mail import send_mail
from resume_maker import settings
from django.http import HttpResponse
from collections import UserString
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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


def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            return render(request, "resume/sign_up.html", {"status": "Mr/Miss. {} your Account created Successfully".format(username)})
        except IntegrityError as e:
            return render(request, "resume/sign_up.html", {"status": "Mr/Miss. {} your Account Already  Exist".format(username)})
    return render(request, "resume/sign_up.html")


def sign_in(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('home')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'resume/sign_in.html')


def mail(user, password):
    subject = "Greetings"
    msg = f"Congratulations for your successfull ResumeForm username {user} ,password {password}"
    to = "nisha.thoughtwin@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "Mail Sent Successfully"
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
        resume = Resume.objects.filter(user=user)
        return render(request, 'resume/dashboard.html', {'resume': resume, })


class FresherResumeInput(View):
    # def get(self, request):
    #     form1 = ResumeForm
    #     form2 = ResumeUserDetailsForm
    #     form3 = EducationFormSet(queryset=Education.objects.none())
    #     form4 = ExperienceForm
    #     form5 = WorkSamplesForms
    #     form6 = SkillsFormSet(queryset=Skills.objects.none())
    #     form7 = HobbiesForm
    #     form8 = CertificateForm
    #     form9 = AchievementsForm
    #     context = {'form1': form1, 'form2': form2,
    #                'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }
    #     return render(request, 'resume/fresher.html', context)

    def post(self, request):
        # print(request.POST)
        print(request.POST.get('template1_id'))
        template_id=request.POST.get('template1_id')
        template =ChooseTemplate.objects.get(id=template_id)

        form1 = ResumeForm(request.POST)

        form2 = ResumeUserDetailsForm(request.POST, request.FILES)

        form3 = EducationFormSet(data=request.POST)
        # print(form3)

        form4 = SkillsFormSet(request.POST, None)
        form5 = HobbiesForm(request.POST)
        form6 = CertificateForm(request.POST)
        form7 = AchievementsForm(request.POST)

        if form1.is_valid and form2.is_valid and form3.is_valid and form4.is_valid and form5.is_valid and form6.is_valid and form7.is_valid:

            resume = form1.save(commit=False)
            resume.template=template

            resume.user = request.user

            resume.save()

            resumeUserDetails = form2.save(commit=False)
            resumeUserDetails.resume = resume

            resumeUserDetails.save()
            for f in form3:

                eductation = f.save(commit=False)
                eductation.resume = resume
                eductation.save()

            for s in form4:

                skills = s.save(commit=False)
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


@method_decorator(login_required, name='dispatch')
class ExperienceResumeInput(View):
    def get(self, request):
        form1 = ResumeForm

        form2 = ResumeUserDetailsForm

        form3 = EducationFormSet

        form4 = ExperienceForm
        form5 = WorkSamplesForms
        form6 = SkillsFormSet
        form7 = HobbiesForm
        form8 = CertificateForm
        form9 = AchievementsForm
        context = {'form1': form1, 'form2': form2,
                   'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }
        return render(request, 'resume/experience.html', context)


@method_decorator(login_required, name='dispatch')
class GenratePdf(View):
    def post(self, request):
        if request.method == 'POST':
            url = request.POST.get('temp_url')
            pdf = pdfkit.from_url(url, 'file1.pdf')
            # resume = Resume.objects.create(resume=pdf)
            return HttpResponse('download success')


@method_decorator(login_required, name='dispatch')
class Template1(View):
    def get(self, request):
        context = {}
        user = request.user
        print(user)
        resume = Resume.objects.get(user=user)
        context['resume'] = resume
        print(resume.education_set.all().first().degree_class)
        # mail(resume)
        return render(request, 'resume/template1.html', context)


@method_decorator(login_required, name='dispatch')
class Template2(View):
    def get(self, request):
        return render(request, 'resume/template2.html')


def logout_request(request):
    logout(request)
    return redirect("/")


class Template3(View):
    def get(self, request):
        context = {}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume'] = resume

        return render(request, 'resume/template3.html', context)


class Template4(View):
    def get(self, request):
        context = {}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume'] = resume

        return render(request, 'resume/template4.html', context)


# poornima....................................................................
class Template5(View):
    def get(self, request):
        context = {}
        user = request.user
        resume = Resume.objects.get(user=user)
        context['resume'] = resume
        print(resume.education_set.all())
        # mail(resume)
        return render(request, 'resume/template5.html', context)


class UpdateFresherData(View):

    @method_decorator(login_required)
    def get(self, request, id):
        resume = Resume.objects.get(pk=id)

        modeleducation = Education.objects.filter(pk=id).first()

        form = EducationForm(instance=modeleducation)

        eduform = EducationForm()
        education = Education.objects.filter(resume=resume)

        context = {'form': form, 'eduform': eduform, 'education': education}

        return render(request, 'resume/updatedata.html', context)

    @method_decorator(login_required)
    def post(self, request, id):

        resume = Resume.objects.get(id=id)

        degree = request.POST.get("degree_class")
        year = request.POST.get("year_of_passing")
        percentage = request.POST.get("percentage_or_grade")
        university = request.POST.get("university")
        addeducation = Education(resume=resume, degree_class=degree, year_of_passing=year,
                                 percentage_or_grade=percentage, university=university)
        addeducation.save()
        print(request.POST)
        print(resume)
        return redirect("dashboard")


class UpdateEducation(View):

    @method_decorator(login_required)
    def post(self, request):

        degree = request.POST.get("degree_class")
        year = request.POST.get("year_of_passing")
        percentage = request.POST.get("percentage_or_grade")
        university = request.POST.get("university")
        print(request.POST)

        updateedu = Education.objects.get(id=request.POST.get('id'))
        updateedu.degree_class = degree
        updateedu.year_of_passing = year
        updateedu.percentage_or_grade = percentage
        updateedu.university = university
        updateedu.save()

        return redirect("dashboard")


   
def choose_template1(request):

    form1 = ResumeForm
    form2 = ResumeUserDetailsForm
    form3 = EducationFormSet(queryset=Education.objects.none())
    form4 = ExperienceForm
    form5 = WorkSamplesForms
    form6 = SkillsFormSet(queryset=Skills.objects.none())
    form7 = HobbiesForm
    form8 = CertificateForm
    form9 = AchievementsForm
   
    template1 ="resume_templates/template1.html"
    choose_template = ChooseTemplate.objects.create(name=template1)
    context = {'form1': form1, 'form2': form2,'template':choose_template,
                'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }


    return render(request,'resume/fresher.html',context)


def choose_template2(request):

    form1 = ResumeForm
    form2 = ResumeUserDetailsForm
    form3 = EducationFormSet(queryset=Education.objects.none())
    form4 = ExperienceForm
    form5 = WorkSamplesForms
    form6 = SkillsFormSet(queryset=Skills.objects.none())
    form7 = HobbiesForm
    form8 = CertificateForm
    form9 = AchievementsForm
   
    template2 ="resume_templates/template2.html"
    choose_template = ChooseTemplate.objects.create(name=template2)
    context = {'form1': form1, 'form2': form2,'template':choose_template,
                'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }


    return render(request,'resume/fresher.html',context)


def choose_template3(request):

    form1 = ResumeForm
    form2 = ResumeUserDetailsForm
    form3 = EducationFormSet(queryset=Education.objects.none())
    form4 = ExperienceForm
    form5 = WorkSamplesForms
    form6 = SkillsFormSet(queryset=Skills.objects.none())
    form7 = HobbiesForm
    form8 = CertificateForm
    form9 = AchievementsForm
   
    template3 ="resume_templates/template3.html"
    choose_template = ChooseTemplate.objects.create(name=template3)
    context = {'form1': form1, 'form2': form2,'template':choose_template,
                'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }


    return render(request,'resume/fresher.html',context)


def choose_template4(request):

    form1 = ResumeForm
    form2 = ResumeUserDetailsForm
    form3 = EducationFormSet(queryset=Education.objects.none())
    form4 = ExperienceForm
    form5 = WorkSamplesForms
    form6 = SkillsFormSet(queryset=Skills.objects.none())
    form7 = HobbiesForm
    form8 = CertificateForm
    form9 = AchievementsForm
   
    template4 ="resume_templates/template4.html"
    choose_template = ChooseTemplate.objects.create(name=template4)
    context = {'form1': form1, 'form2': form2,'template':choose_template,
                'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }


    return render(request,'resume/fresher.html',context)