from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from .models import Project, ProjectImages
from .forms import ContactForm

# Create your views here.
class ContactMixin(FormMixin):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class IndexView(ContactMixin, generic.TemplateView):
    template_name = 'index.html'


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'project.html'
    slug_url_kwarg = "proj"


    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['form'] = ContactMixin
        return context



class GalleryView(ContactMixin, generic.ListView):
    model = Project
    template_name = 'gallery.html'



class SystemView(ContactMixin, generic.TemplateView):
    template_name = 'speakers.html'


class SecurityView(ContactMixin, generic.TemplateView):
    template_name = 'security.html'

class RemoteStartView(ContactMixin, generic.TemplateView):
    template_name = 'remote_start.html'

class NavSystemView(ContactMixin, generic.TemplateView):
    template_name = 'nav_systems.html'

class DetailingView(ContactMixin, generic.TemplateView):
    template_name='detailing.html'


class ContactView(ContactMixin, generic.TemplateView):
    template_name = 'contact.html'


