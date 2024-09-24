from django.contrib import admin

from .models import Courses

class CoursesAdmin(admin.ModelAdmin):
    list_display = 'name', 'description', 'price'
    list_display_links = 'price', 'name'

admin.site.register(Courses, CoursesAdmin)