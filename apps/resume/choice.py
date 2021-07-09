from .models import *

COMPETENCY_CHOICES = (
    ('', '-----'),
    (1, 'Below Average'),
    (2, 'Average'),
    (3, 'Good'),
    (4,'Very Good'),
    (5, 'Excellent'), )
RESUME_CHOICES = (
    ('template1', 'Template1'),
    ('template2', 'Template2'),
    ('template3', 'Template3'),
    ('template4', 'Template4'), )



# def choose_template1(self, request):

#     template_name ="resume_templates/template1.html"
#     choose_template = ChooseTemplate.objects.create(name=template_name)
#     return None