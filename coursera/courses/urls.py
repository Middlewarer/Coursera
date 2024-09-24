from django.urls import path
from .views import IndexView, CoursesListView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path('courses/', CoursesListView.as_view(), name='courses_list_view'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name="courses_detail_view"),
]