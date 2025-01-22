from django.contrib import admin
from .models import UserProfile, Course, Enrollment
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Enrollment)