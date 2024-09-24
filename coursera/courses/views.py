from django.shortcuts import render

from .models import Courses

def index_view(request):
    context = {

    }
    return render(request, 'courses/index.html', context=context)

def courses_list_view(request):
    context = {
        'courses': Courses.objects.all()
    }
    return render(request, 'courses/courses_list.html', context=context)

# Create your views here.
