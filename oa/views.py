from django.shortcuts import render, HttpResponse, redirect
from django.http import request
from django.views import generic
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from .models import Project, ProjectImages
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template






# Create your views here.
class ContactMixin(FormMixin):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'index'


    def form_valid(self, form):
        contact_name = request.POST.get(
            'contact_name'
            , '')
        contact_email = request.POST.get(
            'contact_email'
            , '')
        form_message = request.POST.get('message', '')

        # Email the profile with the contact information
        template = get_template('static/contact_template.txt')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_message': form_message,
        })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "OxAudio.com" + '',
            ['info@oxaudio.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        form.send_email()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            print
            'yes done'
            # save your model
            # redirect

        return super(TemplateView, self).render_to_response(context)

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


