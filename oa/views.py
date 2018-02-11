from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import request
from django.views import generic
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from .models import Project, ProjectImages
from .forms import ContactForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template






# Create your views here.
class ContactMixin(FormMixin):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'index'




    def post(self, request, *args, **kwargs):
        subject = request.POST.get('contact_name', '')
        from_email = request.POST.get('contact_email', '')
        message = request.POST.get('message', '')
        #next = request.POST.get('next', '/')

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['info@oxaudio.com'], fail_silently=False)
                print("success")
                messages.add_message(request, messages.INFO, 'Thanks for contacting us, we will be in touch shortly!.')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


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
    template_name = 'systems.html'


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


