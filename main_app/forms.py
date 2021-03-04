from django.contrib.auth.models import User
from django import forms
from .models import User, Course, Lesson, User_Profile, Quiz, Question

class User_Profile_Form(forms.ModelForm):
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email']
            widgets = {
                'username' : forms.TextInput(attrs={'class':'form-control'}),
                'first_name' : forms.TextInput(attrs={'class':'form-control'}),
                'last_name' :forms.TextInput(attrs={'class':'form-control'}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'password':forms.TextInput(attrs={'class':'form-control'}),
                
            }

class Teacher_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['major' , 'experience' , 'image']
        widgets = {
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class PasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        widgets = {

            'password': forms.TextInput(attrs={'type': 'password'}),
        }

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'subject_title', 'level',
                  'duration', 'description', 'course_image')
        subjects = (
            ('', 'Select a subject'),
            # First one is the value of select option and second is the displayed value in option
            ('programming', 'programming'),
            ('statistic', 'statistic'),
            ('Scince', 'Scince'),
            ('English', 'English'),
        )
        levels = (
            ('', 'Select a levels'),
            # First one is the value of select option and second is the displayed value in option
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
        )
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_title': forms.Select(choices=subjects, attrs={'class': 'form-control'}),
            'level': forms.Select(choices=levels, attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'user': forms.Select(attrs={'class': 'form-control'}),
        }
            

class QuizForm(forms.ModelForm):
    class Meta:
            model = Quiz
            fields = ['quiz_name', 'course']

            widgets = {
                'course' : forms.Select(attrs={'class':'form-control'}),
                'quiz_name' : forms.TextInput(attrs={'class':'form-control'}),
            }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'lesson_link', 'course']
        widgets = {
            'course' : forms.Select(attrs={'class':'form-control'}),
            'lesson_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lesson_link': forms.TextInput(attrs={'class': 'form-control'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
            model = Question
            fields = ['question_name','choices', 'correct_answer']

            widgets = {
                'question_name' : forms.TextInput(attrs={'class':'form-control'}),
                'choices' : forms.TextInput(attrs={'class':'form-control'}),
                'correct_answer' : forms.TextInput(attrs={'class':'form-control'}),
            }

