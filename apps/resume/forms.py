#from .models import *
from django import forms
from .models import Resume, UserExtraFields, Education, Skills, Experience, Hobbies, Certificate, Achievements


# class ResumeForm(forms.ModelForm):
#     class Meta:
#         model = Resume
#         fields = '__all__'

# class UserExtraFieldsForm(forms.ModelForm):
#     class Meta:
#         model = UserExtraFields
#         fields = ['date_of_birth','address','phone','photo']


# class EducationForm(forms.ModelForm):
#     class Meta:
#         model = Education
#         fields = ['name','year_of_passing','percentage_or_grade','university']


# class SkillsForm(forms.ModelForm):
#     class Meta:
#         model = Skills
#         fields = ['name']


# class ExperienceForm(forms.ModelForm):
#     class Meta:
#         model = Experience
#         fields = ['company_name','duration','designation','role','place']


# class HobbiesForm(forms.ModelForm):
#     class Meta:
#         model = Hobbies
#         fields = ['name']


# class CertificateForm(forms.ModelForm):
#     class Meta:
#         model = Certificate
#         fields = ['name']

# class AchievementsForm(forms.ModelForm):
#     class Meta:
#         model = Achievements
#         fields = ['name']
#


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title', 'name': 'title', 'id': 'title'}),
            'objective': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'objective', 'name': 'objective', 'id': 'objective'}),

        }
        fields = "__all__"


class UserExtraFieldsForm(forms.ModelForm):
    class Meta:
        model = UserExtraFields
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'date_of_birth', 'name': 'date_of_birth', 'id': 'date_of_birth'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'phone', 'name': 'phone', 'id': 'phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address', 'name': 'address', 'id': 'address'}),


        }
        fields = ['date_of_birth', 'address', 'phone', 'photo']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['name', 'year_of_passing',
                  'percentage_or_grade', 'university']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name', 'name': 'Name', 'id': 'Name'}),
            'year of passing': forms.DateInpu(attrs={'class': 'form-control', 'placeholder': 'year of passing', 'name': 'year of passing', 'id': 'year of passing'}),
            'grade/percentage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'grade/percentage', 'name': 'grade/percentage', 'id': 'grade/percentage'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'university', 'name': 'university', 'id': 'university'}),


        }


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'name': 'Name', 'id': 'Name'}),

        }
        fields = ['name']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience

        widgets = {
            'company name ': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company name', 'name': 'company name', 'id': 'company name'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'duration', 'name': 'duration', 'id': 'duration'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'designation', 'name': 'designation', 'id': 'designation'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'role', 'name': 'role', 'id': 'role'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'place', 'name': 'place', 'id': 'place'}),

        }
        fields = ['company_name', 'duration', 'designation', 'role', 'place']


class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name', 'name': 'Name', 'id': 'Name'}),
        }
        fields = ['name']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name', 'name': 'Name', 'id': 'Name'}),
        }
        fields = ['name']


class AchievementsForm(forms.ModelForm):
    class Meta:
        model = Achievements

        widgets = {
            'resume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'resume', 'name': 'resume', 'id': 'resume'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name', 'name': 'achievements_name', 'id': 'achievements_name'}),


        }
        fields = ['name']
