import imgkit
import datetime
# from .utils import render_to_pdf
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
# from .utils import render_to_pdf


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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('dashboard')
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
    def get(self, request):
        form1 = ResumeForm
        form2 = ResumeUserDetailsForm
        form3 = EducationFormSet(queryset=Education.objects.none())
        form4 = ExperienceForm
        form5 = WorkSamplesForms
        form6 = SkillsFormSet(queryset=Skills.objects.none())
        form7 = HobbiesForm
        form8 = CertificateForm
        form9 = AchievementsForm
        context = {'form1': form1, 'form2': form2,
                   'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }
        return render(request, 'resume/fresher.html', context)

    def post(self, request):
        # # print(request.POST)
        # print(request.POST.get('template1_id'))
        # template_id=request.POST.get('template1_id')
        # template =ChooseTemplate.objects.get(id=template_id)

        form1 = ResumeForm(request.POST)

        # form2 = ResumeUserDetailsForm(request.POST, request.FILES)

        # form3 = EducationFormSet(data=request.POST)
        # # print(form3)

        # form4 = SkillsFormSet(request.POST, None)
        # form5 = HobbiesForm(request.POST)
        # form6 = CertificateForm(request.POST)
        # form7 = AchievementsForm(request.POST)

        #  and form2.is_valid and form3.is_valid and form4.is_valid and form5.is_valid and form6.is_valid and form7.is_valid:
        if form1.is_valid:
            resume = form1.save(commit=False)
            # resume.template=template

        #     # resume.user = request.user

        #     resumeUserDetails = form2.save(commit=False)
        #     resumeUserDetails.resume = resume

        #     resumeUserDetails.save()
        #     for f in form3:

        #         eductation = f.save(commit=False)
        #         eductation.resume = resume
        #         eductation.save()

        #     for s in form4:

        #         skills = s.save(commit=False)
        #         skills.resume = resume
        #         skills.save()

        #     hobbies = form5.save(commit=False)
        #     hobbies.resume = resume

        #     hobbies.save()
        #     certificate = form6.save(commit=False)
        #     certificate.resume = resume

        #     certificate.save()
        #     achievements = form7.save(commit=False)
        #     achievements.resume = resume

        #     achievements.save()

        if request.user.is_authenticated:
            user = request.user
            resume.user = user
            resume.save()
            return redirect('dashboard')

        else:
            return render(request, 'resume/thank-you.html')


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
        # print(user)
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
        resume = Resume.objects.filter(user=user).last()
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


class ViewResumeDetail(View):
    @method_decorator(login_required)
    def get(self, request, id):
        resume = Resume.objects.get(pk=id)
        print('...........', resume)
        eduform = EducationForm()
        education = Education.objects.filter(resume=resume)

        skillsform = SkillsForm()
        skills = Skills.objects.filter(resume=resume)

        hobbiesform = HobbiesForm()
        hobbies = Hobbies.objects.filter(resume=resume)

        achievementsform = AchievementsForm()
        achievements = Achievements.objects.filter(resume=resume)

        experienceform = ExperienceForm()
        experience = Experience.objects.filter(resume=resume)

        context = {'resume': resume, 'eduform': eduform, 'education': education, 'skillsform': skillsform, 'skills': skills, 'hobbiesform': hobbiesform,
                   'hobbies': hobbies, 'achievementsform': achievementsform, 'achievements': achievements, 'experienceform': experienceform, 'experience': experience}
        return render(request, 'resume/updatedata.html', context)


# poornima...........................................................

class AddEducation(View):
    @method_decorator(login_required)
    def post(self, request):

        resume = Resume.objects.get(pk=request.POST.get('id'))
        qualification = request.POST.get("qualification_name")
        year = request.POST.get("year_of_passing")
        percentage = request.POST.get("percentage_or_grade")
        university = request.POST.get("university")
        addeducation = Education(resume=resume, qualification_name=qualification,
                                 year_of_passing=year, percentage_or_grade=percentage, university=university)

        addeducation.save()
        print(request.POST)

        return redirect("updateresume", id=resume.id)


class UpdateEducation(View):

    @method_decorator(login_required)
    def post(self, request):

        degree = request.POST.get("qualification_name")
        year = request.POST.get("year_of_passing")
        percentage = request.POST.get("percentage_or_grade")
        university = request.POST.get("university")

        upd_education = Education.objects.get(id=request.POST.get('id'))
        upd_education.qualification_name = degree
        upd_education.year_of_passing = year
        upd_education.percentage_or_grade = percentage
        upd_education.university = university
        upd_education.save()

        print(request.POST)
        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)


class DeleteEducation(View):

    def post(self, request):
        edu = Education.objects.get(id=request.POST.get("e_id"))
        edu.delete()
        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)


# poornima...........................................................

class AddSkillsData(View):
    @method_decorator(login_required)
    @method_decorator(login_required)
    def post(self, request, *args):
        resume_id = request.POST.get("id")

        resume = Resume.objects.get(id=resume_id)
        skills = request.POST.get("skills")
        addskills = Skills(resume=resume)
        addskills.skills = skills
        addskills.save()

        return redirect("updateresume", id=resume.id)


class UpdateSkills(View):

    @method_decorator(login_required)
    def post(self, request):
        skill = Skills.objects.get(id=request.POST.get("id"))
        skill.skills = request.POST.get("skills")
        skill.save()

        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)


class DeleteSkills(View):
    @method_decorator(login_required)
    def get(self, request, id):

        skills = Skills.objects.get(id=id)

        skills.delete()

        return HttpResponseRedirect("/dashboard/")
# ..................................................................


class AddHobbiesData(View):

    @method_decorator(login_required)
    def post(self, request):
        resume = Resume.objects.get(id=request.POST.get("id"))
        print(resume.id)
        hobbies = request.POST.get("hobbies")
        addhobbies = Hobbies(resume=resume)
        addhobbies.hobbies = hobbies
        addhobbies.save()
        print(request.POST)
        print(resume)
        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume.id)


class UpdateHobbies(View):

    @method_decorator(login_required)
    def post(self, request):
        hobbie = Hobbies.objects.get(id=request.POST.get("id"))
        hobbie.hobbies = request.POST.get("hobbies")
        hobbie.save()

        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)


class DeleteHobbies(View):
    @method_decorator(login_required)
    def get(self, request, id):
        hobbies = Hobbies.objects.get(id=id)
        hobbies.delete()
        return redirect("dashboard")

# .................................................................


class AddAchievementsData(View):

    @method_decorator(login_required)
    def post(self, request):
        resume = Resume.objects.get(id=request.POST.get("id"))
        print(resume.id)
        achievements = request.POST.get("achievements")
        addachievements = Achievements(resume=resume)
        addachievements.achievements = achievements
        addachievements.save()
        print(request.POST)
        print(resume)

        return redirect("updateresume", id=resume.id)


class UpdateAchievements(View):

    @method_decorator(login_required)
    def post(self, request):
        achievement = Achievements.objects.get(id=request.POST.get("id"))
        achievement.achievements = request.POST.get("achievements")
        achievement.save()

        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)


class DeleteAchievements(View):
    @method_decorator(login_required)
    def get(self, request, id):
        achievements = Achievements.objects.get(id=id)
        achievements.delete()
        return HttpResponseRedirect("/dashboard")
# ..................................................................


class AddExperienceData(View):
    @method_decorator(login_required)
    def post(self, request):

        resume = Resume.objects.get(pk=request.POST.get('id'))
        company_name = request.POST.get("company_name")
        designation = request.POST.get("designation")
        role = request.POST.get("role")
        place = request.POST.get("place")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        addexperience = Experience(resume=resume, company_name=company_name, designation=designation,
                                   start_date=start_date, end_date=end_date, role=role, place=place)

        addexperience.save()
        print(request.POST)

        return redirect("updateresume", id=resume.id)


class UpdateExperience(View):

    @method_decorator(login_required)
    def post(self, request):
        experience = Experience.objects.get(id=request.POST.get("id"))
        experience.company_name = request.POST.get("company_name")
        experience.designation = request.POST.get("designation")
        experience.role = request.POST.get("role")
        experience.place = request.POST.get("place")
        experience.start_date = request.POST.get("start_date")
        experience.end_date = request.POST.get("end_date")

        experience.save()

        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)


class DeleteExperience(View):
    @method_decorator(login_required)
    def post(self, request):
        experience = Experience.objects.get(id=request.POST.get("ex_id"))
        experience.delete()
        resume_id = request.POST.get("r_id")
        return redirect("updateresume", id=resume_id)

# ..............................................................................


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

    template1 = "resume_templates/template1.html"
    choose_template = ChooseTemplate.objects.create(name=template1)
    context = {'form1': form1, 'form2': form2, 'template': choose_template,
               'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }

    return render(request, 'resume/fresher.html', context)


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

    template2 = "resume_templates/template2.html"
    choose_template = ChooseTemplate.objects.create(name=template2)
    context = {'form1': form1, 'form2': form2, 'template': choose_template,
               'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }

    return render(request, 'resume/fresher.html', context)


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

    template3 = "resume_templates/template3.html"
    choose_template = ChooseTemplate.objects.create(name=template3)
    context = {'form1': form1, 'form2': form2, 'template': choose_template,
               'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }

    return render(request, 'resume/fresher.html', context)


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

    template4 = "resume_templates/template4.html"
    choose_template = ChooseTemplate.objects.create(name=template4)
    context = {'form1': form1, 'form2': form2, 'template': choose_template,
               'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, }

    return render(request, 'resume/fresher.html', context)


class GenratePdf(View):

    def get(self, request):

        imgkit.from_url('127.0.0.1:8000/resume4/', 'out.jpg')
        return HttpResponse('done')
