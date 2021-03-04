# main_app/urls.py
from django.urls import path
from main_app import views
from django.contrib.auth import views as auth_views  

urlpatterns = [
    path('teacher/profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('lessons/<int:courseId>', views.courseDetails, name='lessons'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('takeQuiz/<int:question_id>', views.takeQuiz, name='takeQuiz'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name='password_reset_complete'),
    path('TeacherCourses/create/', views.CourseCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/update/<int:pk>', views.CourseUpdate.as_view(), name='addCourse_create'),
    path('TeacherCourses/<int:user_id>/', views.CoursesTeacher, name='courses_teacher'),
    path('quiz/<int:course_id>/', views.ShowQuiz, name='course_quiz'),
    path('TeacherCourses/lesson/create/', views.LessonCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/quiz/create/', views.QuizCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/delete/<int:pk>', views.CourseDelete.as_view(), name='addCourse_create'),
    path('GetQuiz/' , views.getQuizes, name='Quizes'),
    path('profile/<int:pk>/update', views.profileUpdate.as_view(), name='User_Profile'),
    path('enroll/<int:course_id>/' , views.EnrollCourse, name='Enroll'),
    path('',views.courseView, name='courseView'),
    path('courses/', views.EnrolledCourses, name='addCourse_create'),
    path('change_password/', views.change_password, name="change_password"),

]
