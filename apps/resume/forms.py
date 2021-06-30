#from .models import *
from django import forms
from .models import Resume, Education,Skills,Experience,Hobbies,Certificate,Achievements


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
            #'user' : forms.TextInput(attrs={'class':'form-control','placeholder':'user'}),
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'title','name':'title','id':'title'}),
            'description' : forms.TextInput(attrs={'class':'form-control','placeholder':'description','name':'title','id':'title'}),
            'skills': forms.TextInput(attrs={'class':'form-control','placeholder':'skills','name':'title','id':'title'}),
            'education' : forms.TextInput(attrs={'class':'form-control','placeholder':'education','name':'title','id':'title'}),
            'certifications' : forms.TextInput(attrs={'class':'form-control','placeholder':'certifications','name':'title','id':'title'}),
            'experience' : forms.TextInput(attrs={'class':'form-control','placeholder':'experience','name':'title','id':'title'}),
            'hobbies' : forms.TextInput(attrs={'class':'form-control','placeholder':'hobbies','name':'title','id':'title'}),
            'acheivments' : forms.TextInput(attrs={'class':'form-control','placeholder':'acheivments','name':'title','id':'title'}),

        }
        fields = "__all__"



class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        widgets = {
        
            'resume' : forms.TextInput(attrs={'class':'form-control','placeholder':'resume','name':'resume','id':'resume'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'name','name':'Name','id':'Name'}),
            'year of passing' : forms.TextInput(attrs={'class':'form-control','placeholder':'year of passing','name':'year of passing','id':'year of passing'}),
            'grade/percentage' : forms.TextInput(attrs={'class':'form-control','placeholder':'grade/percentage','name':'grade/percentage','id':'grade/percentage'}),
        }




class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        widgets = {
            'resume' : forms.TextInput(attrs={'class':'form-control','placeholder':'resume','name':'resume','id':'resume'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name','name':'Name','id':'Name'}),

        }
  
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'resume' : forms.TextInput(attrs={'class':'form-control','placeholder':'resume','name':'resume','id':'resume'}),
            'company name ' : forms.TextInput(attrs={'class':'form-control','placeholder':'company name','name':'company name','id':'company name'}),
            'duration' : forms.TextInput(attrs={'class':'form-control','placeholder':'duration','name':'duration','id':'duration'}),
            'designation' : forms.TextInput(attrs={'class':'form-control','placeholder':'designation','name':'designation','id':'designation'}),
            'role' : forms.TextInput(attrs={'class':'form-control','placeholder':'role','name':'role','id':'role'}),
            'place' : forms.TextInput(attrs={'class':'form-control','placeholder':'place','name':'place','id':'place'}),

        }




class HobbiesForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        fields = '__all__'
        widgets = {
            'resume' : forms.TextInput(attrs={'class':'form-control','placeholder':'resume','name':'resume','id':'resume'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'name','name':'Name','id':'Name'}),
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        widgets = {
            'resume' : forms.TextInput(attrs={'class':'form-control','placeholder':'resume','name':'resume','id':'resume'}),
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'name','name':'Name','id':'Name'}),
        }


class AchievementsForm(forms.ModelForm):
    class Meta:
        model = Achievements
        fields = '__all__'
        widgets = {
            'resume' : forms.TextInput(attrs={'class':'form-control','placeholder':'resume','name':'resume','id':'resume'}),
            'achievements_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'achievements_name','name':'achievements_name','id':'achievements_name'}),
            'descriptions' : forms.TextInput(attrs={'class':'form-control','placeholder':'descriptions','name':'descriptions','id':'descriptions'}),


        }


