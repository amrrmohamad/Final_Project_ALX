from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_TYPES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.user.username

    def is_teacher(self):
        return self.user_type == 'teacher'

    def is_student(self):
        return self.user_type == 'student'


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'})
    video = models.FileField(upload_to='course_videos/', blank=True, null=True, default='course_videos/default.mp4')

    def __str__(self):
        return self.title

    def get_video_url(self):
        if self.video:
            return self.video.url
        return '/media/course_videos/default.mp4'


class Enrollment(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
