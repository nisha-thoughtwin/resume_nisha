from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
import pdfkit
from .models import *
from .forms import *

class Home(View):

    def get(self, request):
        return render(request,'resume/index.html')

class FresherResumeInput(View):

    def get(self, request):
        return render(request,'resume/fresher.html')

class ExperienceResumeInput(View):
    
    def get(self, request):
        return render(request,'resume/experience.html')


    

class GenratePdf(View):
    
    def post(self, request):

        if request.method == 'POST':
            url = request.POST.get('temp_url')
            pdf= pdfkit.from_url(url,'file1.pdf')
            # resume = Resume.objects.create(resume=pdf) 
            return HttpResponse('download success')

class Template2(View):
    def get(self, request):
        return render(request,'resume/template2.html')

    