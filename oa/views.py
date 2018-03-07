from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import request
from django.views import generic
from django.views.generic.base import TemplateView, ContextMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from .models import Project, ProjectImages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.contrib import messages
from django.urls import reverse





# Create your views here.
class ContactMixin(FormMixin):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'index'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            subject = request.POST.get('contact_name', '')
            from_email = request.POST.get('contact_email', '')
            message = request.POST.get('message', '')
            phone_number = request.POST.get('phone_number',"")
            email_content = "Dear Oxaudio"+"\n" + "FROM: "+subject+ "\n"+ "PHONE NUMBER: " + phone_number +'\n'+message

            try:
                send_mail(subject, email_content, from_email, ['ryan@oxaudio.com'], fail_silently=False)
                messages.add_message(request, messages.INFO, 'Thanks for contacting us, we will be in touch shortly!.')
                print("success")

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)



    # def post(self, request, *args, **kwargs):

    #     subject = request.POST.get('contact_name', '')
    #     from_email = request.POST.get('contact_email', '')
    #     message = request.POST.get('message', '')
    #     phone_number = request.POST.get('phone_number',"")
    #     email_content = "Dear Oxaudio"+"\n" + "FROM: "+subject+ "\n"+ "PHONE NUMBER: " + phone_number +'\n'+message

    #     try:
    #         send_mail(subject, email_content, from_email, ['ryan@oxaudio.com'], fail_silently=False)
    #         messages.add_message(request, messages.INFO, 'Thanks for contacting us, we will be in touch shortly!.')
    #         print("success")

    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')


    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class IndexView(ContactMixin, generic.TemplateView):
    template_name = 'index.html'


class ProjectView(ContactMixin, generic.DetailView):
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

class TintView(ContactMixin, generic.TemplateView):
    template_name = 'tint.html'

class ContactView(ContactMixin, generic.TemplateView):
    template_name = 'contact.html'

class PrivacyView(TemplateView):
    template_name = 'privacypolicy.html'
