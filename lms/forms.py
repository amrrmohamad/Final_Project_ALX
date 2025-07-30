from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Course

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=[('teacher', 'Teacher'), ('student', 'Student')])

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'video']
