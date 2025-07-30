import os
import django
import random
from faker import Faker

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from lms.models import UserProfile, Course

fake = Faker()

def create_teacher():
    """Create a fake teacher."""
    user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='password123'
    )
    teacher_profile = UserProfile.objects.create(user=user, user_type='teacher')
    return teacher_profile

def create_student():
    """Create a fake student."""
    user = User.objects.create_user(
        username=fake.user_name(),
        email=fake.email(),
        password='password123'
    )
    student_profile = UserProfile.objects.create(user=user, user_type='student')
    return student_profile

def create_course(teacher_profile):
    """Create a fake course for the given teacher."""
    course = Course.objects.create(
        title=fake.sentence(nb_words=3),
        description=fake.paragraph(nb_sentences=5),
        created_by=teacher_profile
    )
    return course

def populate_data(num_teachers=5, num_students=20, num_courses_per_teacher=3):
    """Populate the database with fake data."""
    for _ in range(num_teachers):
        teacher = create_teacher()
        print(f'Created teacher: {teacher.user.username}')

        # Create courses for the teacher
        for _ in range(num_courses_per_teacher):
            course = create_course(teacher)
            print(f'-- Created course: {course.title}')

    # Create students
    for _ in range(num_students):
        student = create_student()
        print(f'Created student: {student.user.username}')

if __name__ == '__main__':
    print("Populating the database with fake data...")
    populate_data()
    print("Populating complete.")
