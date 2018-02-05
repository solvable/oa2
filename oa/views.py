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




class SystemView(generic.TemplateView):
    template_name = 'speakers.html'


class SecurityView(generic.TemplateView):
    template_name = 'security.html'

class RemoteStartView(generic.TemplateView):
    template_name = 'remote_start.html'

class NavSystemView(generic.TemplateView):
    template_name = 'nav_systems.html'

class DetailingView(generic.TemplateView):
    template_name='detailing.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'

