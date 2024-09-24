from django.urls import path
from .views import index_view, courses_list_view

app_name = 'courses'

urlpatterns = [
    path("", index_view, name='index_view'),
    path('courses/', courses_list_view, name='courses_list_view'),
]