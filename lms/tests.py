from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Course, Enrollment
from django.urls import reverse

class ModelsTestCase(TestCase):

    def setUp(self):
        # Create a teacher user and profile
        teacher_user = User.objects.create_user(username="teacher1", password="password123")
        self.teacher_profile = UserProfile.objects.create(user=teacher_user, user_type="teacher")

        # Create a student user and profile
        student_user = User.objects.create_user(username="student1", password="password123")
        self.student_profile = UserProfile.objects.create(user=student_user, user_type="student")

        # Create a course by the teacher
        self.course = Course.objects.create(
            title="Django Basics",
            description="Learn the basics of Django framework.",
            created_by=self.teacher_profile,
        )

        # Create a user to test login functionality
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")

    def test_user_profile_creation(self):
        self.assertEqual(self.teacher_profile.user.username, "teacher1")
        self.assertTrue(self.teacher_profile.is_teacher())
        self.assertFalse(self.teacher_profile.is_student())

        self.assertEqual(self.student_profile.user.username, "student1")
        self.assertFalse(self.student_profile.is_teacher())
        self.assertTrue(self.student_profile.is_student())

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Django Basics")
        self.assertEqual(self.course.created_by, self.teacher_profile)

    def test_enrollment_creation(self):
        # Enroll the student in the course
        enrollment = Enrollment.objects.create(student=self.student_profile, course=self.course)
        self.assertEqual(enrollment.student, self.student_profile)
        self.assertEqual(enrollment.course, self.course)

    def test_course_video_url(self):
        # Test default video URL
        self.assertEqual(self.course.get_video_url(), "/media/course_videos/default.mp4")

        # Update course video and test URL
        self.course.video = "course_videos/default.mp4"
        self.course.save()
        self.assertEqual(self.course.get_video_url(), "course_videos/default.mp4")

    def test_signup(self):
        # Test the signup process using the RegistrationForm
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'user_type': 'student',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        
        # Check that the signup was successful
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username="newuser").exists())
        
        # Verify the user type (student or teacher)
        new_user = User.objects.get(username="newuser")
        self.assertEqual(new_user.userprofile.user_type, 'student')

    def test_signup_invalid_password(self):
        # Test invalid password mismatch
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'user_type': 'student',
            'password1': 'securepassword123',
            'password2': 'mismatchpassword',
        })
        
        # Ensure the user is not created
        self.assertEqual(response.status_code, 200)  # Stay on the signup page
        self.assertFalse(User.objects.filter(username="newuser").exists())

    def test_login_successful(self):
        # Test successful login
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123',
        })
        
        # Verify login is successful
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        
        # Verify login fails
        self.assertEqual(response.status_code, 200)  # Stay on the login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        # Log the user in first
        self.client.login(username="testuser", password="password123")
        
        # Verify the user is logged in
        self.assertTrue(self.client.session['_auth_user_id'])
        
        # Test logout
        response = self.client.get(reverse('logout'))
        
        # Verify the user is logged out
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertNotIn('_auth_user_id', self.client.session)
