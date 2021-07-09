from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.forms import formset_factory,modelformset_factory



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name', 'name': 'fname', 'id': 'fname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name', 'name': 'lname', 'id': 'lname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email', 'name': 'email', 'id': 'email'}),

        }
        fields = ('first_name', 'last_name', 'email','username','password')


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title', 'name': 'title', 'id': 'title'}),
            'objective': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'objective', 'name': 'objective', 'id': 'objective'}),

        }
        fields = ("title", "objective")


class ResumeUserDetailsForm(forms.ModelForm):
    class Meta:
        model = ResumeUserDetails
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name', 'name': 'first_name', 'id': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name', 'name': 'last_name', 'id': 'last_name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email', 'name': 'email', 'id': 'email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mobile', 'name': 'mobile', 'id': 'mobile'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'name': 'date_of_birth', 'id': 'date_of_birth'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address', 'name': 'address', 'id': 'address'}),


        }
        fields = ['first_name', 'last_name','email', 'mobile','date_of_birth', 'address', 'photo']


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education

        fields = ['qualification_name', 'year_of_passing',
                  'percentage_or_grade', 'university']

        widgets = {

            'qualification_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your qualification name', 'name': 'qualification', 'id': 'qualification',}),
            'year of passing': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'year of passing', 'name': 'year_of_passing', 'id': 'year_of_passing'}),
            'percentage_or_grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'grade/percentage', 'name': 'percentage', 'id': 'percentage'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'university', 'name': 'university', 'id': 'university'}),


        }


# EducationFormSet = formset_factory(EducationForm,extra=1,max_num=None,  )

EducationFormSet = modelformset_factory(Education,fields=("qualification_name","year_of_passing","percentage_or_grade","university"),extra=1)


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience

        widgets = {
            'company name ': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company name', 'name': 'company_name', 'id': 'company_name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'designation', 'name': 'designation', 'id': 'designation'}),
            'role': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'role', 'name': 'role', 'id': 'role'}),
            'place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'place', 'name': 'place', 'id': 'place'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'name': 'start_date', 'id': 'start_date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'name': 'end_date', 'id': 'end_date'}),

        }
        fields = ['company_name', 'designation','start_date','end_date', 'role', 'place']

ExperienceFormSet = formset_factory(ExperienceForm,extra=1,max_num=None)


class WorkSamplesForms(forms.ModelForm):

     class Meta:
        model = WorkSamples

        widgets = {
            'project_name ': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'project name', 'name': 'project_name', 'id': 'project_name'}),
            'project_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'project link', 'name': 'project_link', 'id': 'project_link'}),
            'technology': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'technology use', 'name': 'technology', 'id': 'technology'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description', 'name': 'description', 'id': 'description'}),
            'responsibilities': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'responsibilities', 'name': 'responsibilities', 'id': 'responsibilities'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'name': 'date', 'id': 'date'}),

        }

        fields = ['project_name','project_link','technology','description','responsibilities','date']
        




class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills

        widgets = {
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your skills ', 'skills': 'Name', 'id': 'skills'}),

        }
        fields = ['skills'] 

# SkillsFormSet = formset_factory(SkillsForm,extra=1,max_num=None)
SkillsFormSet = modelformset_factory(Skills,fields=("skills",),extra=1 )



   


class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies

        widgets = {
            'hobbies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Hobbies', 'name': 'hobbies', 'id': 'hobbies'}),
        }
        fields = ['hobbies']

HobbiesFormSet = formset_factory(HobbiesForm,extra=1,max_num=None)



class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate

        widgets = {
            'certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certificate', 'name': 'certificate', 'id': 'certificate'}),
        }
        fields = ['certificate']

CertificateFormSet = formset_factory(CertificateForm,extra=1,max_num=None)



class AchievementsForm(forms.ModelForm):
    class Meta:
        model = Achievements

        widgets = {
            'achievements': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Achievements', 'name': 'achievements', 'id': 'achievements'}),


        }
        fields = ['achievements']
AchievementsFormSet = formset_factory(AchievementsForm,extra=1,max_num=None)
