from django.contrib import admin

from apps.resume.models import *


class EducationAdmin(admin.ModelAdmin):
    readonly_fields = ('year_of_passing',)
    search_fields = ['name', ]
    list_filter = ['percentage_or_grade', ]
    list_display = ['resume','name', 'percentage_or_grade', 'university', ]


class ExperienceAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'designation', ]
    list_filter = ['designation', ]
    list_display = ['resume','company_name', 'duration', 'designation','role','place' ]


class HobbiesAdmin(admin.ModelAdmin):
    search_fields = ['resume', ]
    list_display = ['resume', 'name', ]


class SkillAdmin(admin.ModelAdmin):
    search_fields = ['resume', ]
    list_display = ['resume', 'name', ]


class CertificateAdmin(admin.ModelAdmin):
    search_fields = ['resume', ]
    list_display = ['resume', 'name', ]



class AchievementsAdmin(admin.ModelAdmin):
    search_fields = ['resume', ]
    list_display = ['resume', 'name', ]


admin.site.register(Resume)
admin.site.register(UserExtraFields)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Hobbies, HobbiesAdmin)
admin.site.register(Skills, SkillAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Achievements, AchievementsAdmin)



