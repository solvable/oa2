from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Project, ProjectImages


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'project.html'
    slug_url_kwarg = "proj"




class GalleryView(generic.ListView):
    model = Project
    template_name = 'gallery.html'

class StereoView(generic.TemplateView):
    template_name = 'stereo.html'