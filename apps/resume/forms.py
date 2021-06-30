from .models import *
from django import forms


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'

class UserExtraFieldsForm(forms.ModelForm):
    class Meta:
        model = UserExtraFields
        fields = ['date_of_birth','address','phone','photo']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name','year_of_passing','percentage_or_grade','university']
       


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['name']
       

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name','duration','designation','role','place']
        

class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields = ['name']
        

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name']

class AchievementsForm(forms.ModelForm):
    class Meta:
        model = Achievements
        fields = ['name']
        