# from .models import *
# from django import forms


# class ResumeCommonDetailsForm(forms.ModelForm):

#     class Meta:

#         model = Resume
#         fields = ('first_name', 'last_name', 'date_of_birth',
#                   'email', 'phone', 'address')

#         widgets = {

#             'first_name': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'First Name',
#                 'id': "first-name"}),
#             'last_name': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Last Name',
#                 'id': "last-name"}),
#             'date_of_birth': forms.DateInput(attrs={
#                 'class': "form-control",
#                 'id': "date-of-birth"}),
#             'email': forms.EmailInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Email',
#                 'id': "email"}),
#             'phone': forms.NumberInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'phone or mobile',
#                 'id': "phone"}),
#             'address': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Address',
#                 'id': "address"}),
#         }


# class StudentResumeForm(forms.ModelForm):

#     class Meta:

#         model = StudentResume
#         fields = ('high_school', 'high_secondary_school', 'graduation_level',
#                   'skills', 'hobbies', 'training_programs', 'objective', 'photo')

#         widgets = {

#             'high_school': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'High school name',
#                 'id': "high-school"}),
#             'graduation_level': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'highest graduation',
#                 'id': "graduation-level"}),
#             'skills': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'skills',
#                 'id': "skills"}),
#             'hobbies': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'hobbies',
#                 'id': "hobbies"}),
#             'training_programs': forms.NumberInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'training_programs',
#                 'id': "training_programs"}),
#             'objective': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Your objective',
#                 'id': "objective"}),
#             'photo': forms.FileInput(attrs={
#                 'class': "form-control",
#                 'id': "photo"}),

#         }


# class ExperienceCandidateForm(forms.ModelForm):

#     class Meta:

#         model = ExperienceCandidate
#         fields = ('current_employer', 'work_experience',
#                   'last_designation', 'known_technology')

#         widgets = {

#             'current_employer': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Current Employer',
#                 'id': "first-name"}),
#             'work_experience': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Work Experience ',
#                 'id': "work-experience"}),
#             'last_designation': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'First Name',
#                 'id': "designation-name"}),
#             'known_technology': forms.TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Known_technology',
#                 'id': "technology-name"}),
#         }
