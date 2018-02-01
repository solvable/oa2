from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectView(TemplateView):
    template_name= 'project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project']=get_object_or_404(Project, id=self.kwargs['project'])

class GalleryView(generic.ListView):
    model= Project
    template_name = 'gallery.html'