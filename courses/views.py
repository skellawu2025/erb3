from django.shortcuts import render, redirect

from .models import Course
from .choices import course_code_choices, course_name_choices, location_choices, start_date_choices, fee_choices


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')



def course(request, course_id=None):
    if course_id is not None:
        course = Course.objects.get(id=course_id)
        context = {'course': course}
        return render(request, 'pages/course.html', context)
    else:
        return redirect('index')

def accounts(request):
    return render(request, 'pages/accounts.html')

def search(request):
    return render(request, 'pages/search.html')

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('course/', views.course, name='course'),
    path('course/<int:course_id>', views.course, name='course'),
    path('accounts/', views.accounts, name='accounts'),
    path('search/', views.search, name='search'),
    # path('moreinfo/', views.moreinfo, name='moreinfo'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

