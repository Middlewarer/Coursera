from django.urls import path
from .views import IndexView, CoursesListView

app_name = 'courses'

urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path('courses/', CoursesListView.as_view(), name='courses_list_view'),
]