from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Course

# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'blog/home.html'