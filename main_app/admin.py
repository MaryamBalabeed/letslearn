from django.contrib import admin
from .models import Course, Lesson,User_Profile, Quiz, Question

# Register your models here.

admin.site.register(User_Profile)
# START Maryam Work 
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
# END Maryam Work 