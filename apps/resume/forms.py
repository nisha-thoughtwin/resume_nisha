from django import forms
from .models import Resume, UserExtraFields, Education, Skills, Experience, Hobbies, Certificate, Achievements
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.forms import formset_factory

# class CustomUserCreationForm(UserCreationForm):
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if len(username) < 5:
#             raise forms.ValidationError("Your username is too short. A username must be at least 8 characters long")
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Your username is already taken")
#         return username

# def clean_password1(self):
#     password1 = self.cleaned_data['password1']
#     if validate_password(password1):
#         raise forms.ValidationError('This password is not valid')
#     return password1

# def clean(self, *args, **kwargs):
#     password1 = self.cleaned_data.get("password1")
#     password2 = self.cleaned_data.get("password2")

#     if password1 != password2:
#         raise forms.ValidationError("Your passwords do not match. Please try again")
#     return super(UserCreationForm, self).clean(*args, **kwargs)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name', 'name': 'fname', 'id': 'fname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name', 'name': 'lname', 'id': 'lname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email', 'name': 'email', 'id': 'email'}),

        }
        fields = ('first_name', 'last_name', 'email')


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title', 'name': 'title', 'id': 'title'}),
            'objective': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'objective', 'name': 'objective', 'id': 'objective'}),

        }
        fields = ("title", "objective")


class UserExtraFieldsForm(forms.ModelForm):
    class Meta:
        model = UserExtraFields
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'name': 'date_of_birth', 'id': 'date_of_birth'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'phone', 'name': 'phone', 'id': 'phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address', 'name': 'address', 'id': 'address'}),


        }
        fields = ['date_of_birth', 'address', 'phone', 'photo']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree_class', 'year_of_passing',
                  'percentage_or_grade', 'university']

        widgets = {

            'degree_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your degree or class name', 'name': 'Name', 'id': 'Name'}),
            'year of passing': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'year of passing', 'name': 'year of passing', 'id': 'year of passing'}),
            'percentage_or_grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'grade/percentage', 'name': 'grade/percentage', 'id': 'grade/percentage'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'university', 'name': 'university', 'id': 'university'}),


        }


EducationFormSet = formset_factory(EducationForm,extra=2)


class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills

        widgets = {
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your skills ', 'name': 'Name', 'id': 'Name'}),

        }
        fields = ['skills']


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
            'hobbies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Hobbies', 'name': 'Name', 'id': 'Name'}),
        }
        fields = ['hobbies']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate

        widgets = {
            'certificate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Certificate', 'name': 'Name', 'id': 'Name'}),
        }
        fields = ['certificate']


class AchievementsForm(forms.ModelForm):
    class Meta:
        model = Achievements

        widgets = {
            'achievements': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Achievements', 'name': 'achievements_name', 'id': 'achievements_name'}),


        }
        fields = ['achievements']
