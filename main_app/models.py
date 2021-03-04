from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
# Create your models here.

DEFAULT = '../media/default.png'


#


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    experience = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', default='default.png')

    # def set_image_to_default(self):
    #     self.image.delete(save=False)  # delete old image file
    #     self.image = DEFAULT
    #     self.save()

    def __str__(self):
        return self.user.username


# img profile shahad


class Course(models.Model):

    # START Maryam Work
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,  default='Description')
    course_image = models.ImageField(
        upload_to='images/', null=True, blank=True)
    subject_title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name
# END Maryam Work


class Lesson(models.Model):

    lesson_name = models.CharField(max_length=100)
    lesson_link = models.CharField(max_length=2000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name


class Enrollment(models.Model):

    enrollment_date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Quiz(models.Model):

    quiz_name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):

    question_name = models.CharField(max_length=1000)
    choices = ArrayField(models.CharField(max_length=200), blank=True)
    correct_answer = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class User_Answer(models.Model):

    score = models.IntegerField()
    learner_answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
