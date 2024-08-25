from django.contrib import admin
from .models import FacultyMember
from .models import StudentMember

admin.site.register(FacultyMember)
admin.site.register(StudentMember)