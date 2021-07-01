from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
   
    title = models.CharField(max_length=50)
    objective = models.TextField(max_length=400)

    def __str__(self):
        return str(self.title)
        

class UserExtraFields(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/' ,blank=True)

    def __str__(self):
        return str(self.user)


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    degree_class = models.CharField(max_length=100)
    year_of_passing = models.CharField(max_length=100)
    percentage_or_grade = models.CharField(max_length=100)
    university = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Hobbies(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    hobbies = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skills = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Certificate(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=100)

    def __str__(self):
        return str(self.resume)


class Achievements(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    achievements = models.CharField(max_length=200)

    def __str__(self):
        return str(self.resume)
