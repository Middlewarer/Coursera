from django.shortcuts import render
from django.views import View

from .models import Courses

#IndexView ---> Default page
class IndexView(View):
    template_name = "courses/index.html"

    def get(self, request):
        return render(request, self.template_name)
    
#CoursesListView ----> Page with the lists of the main courses
class CoursesListView(View):
    template_name = "courses/courses_list.html"

    def get(self, request):
        objects = Courses.objects.all()
        return render(request, self.template_name, {'courses': objects})