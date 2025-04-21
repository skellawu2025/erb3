# from django.shortcuts import render
# from django.http import HttpResponse
# from courses.models import Course
# from tutors.models import Tutor
# from courses.choices import course_code_choices, course_name_choices, location_choices
# # Create your views here.
# def index(request):
#     courses = Course.objects.order_by('-published_date').filter(is_published=True)[:3]
#     context = {'courses' : courses,
#               'course_code_choices' : course_code_choices,
#                 'course_name_choices' : course_name_choices,
#                 'location_choices' : location_choices,}
#     return render(request, 'pages/index.html', context)

# def about(request):
#     tutors = Tutor.objects.order_by('-hire_date')
#     registered_tutors = tutors.object.all().filter(is_registered=True)
#     context = {'tutors' : tutors, "registered_tutors" : registered_tutors}
#     return render(request, 'pages/about.html', context)

# def course(request):
#     return render(request, 'pages/course.html')

# def accounts(request):
#     return render(request, 'pages/accounts.html')

from django.shortcuts import render
from tutors.models import Tutor
from pages.models import Page

def about(request):
    tutors = Tutor.objects.order_by('-hire_date')
    registered_tutors = tutors.filter(is_registered=True)
    pages = Page.objects.all()
    context = {
        'pages': pages,
        'tutors': tutors,
        'registered_tutors': registered_tutors
    }
    return render(request, 'pages/about.html', context)
