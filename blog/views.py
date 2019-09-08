from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Course,CourseDetail

# Create your views here.
class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'blog/home.html'

class CourseDetailView(DetailView):
    model = CourseDetail
    context_object_name = 'Detailcourse'
    template_name = 'blog/detail.html'
