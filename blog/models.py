from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=256)
    course_link = models.URLField()
    img_link = models.URLField()
    website = models.URLField()
    course_content = models.CharField(max_length=150)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CourseDetail(models.Model):
    description = models.TextField()
    whatyouwilllearn = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.course.name

