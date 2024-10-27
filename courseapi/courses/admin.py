from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['id', 'name']
    search_fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    list_filter = ['id', 'subject']
    search_fields = ['subject']


class LessonAdmin(admin.ModelAdmin):
    list_filter = ['id', 'subject']
    search_fields = ['subject']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)