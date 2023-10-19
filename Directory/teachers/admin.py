from django.contrib import admin
from .models import Teacher
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','profile_picture','email','phone','room_number','employee_number','subjects_taught')

admin.site.register(Teacher,TeacherAdmin)