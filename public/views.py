from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.template.loader import get_template
from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from public.models import Contact
from public.forms import ContactForm

from_email = settings.DEFAULT_FROM_EMAIL
admin_emails = settings.ADMIN_LIST_EMAILS

def get_admin_url(request):
    admin_url = reverse('admin:index')
    return admin_url


class HomeView(TemplateView):
    template_name = "public/views/home.html"


class ServiceView(TemplateView):
    template_name = "public/views/service.html"


class WorkView(TemplateView):
    template_name = "public/views/work.html"


class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_message = "Thank you for contacting us your request is successfully registered"
    success_url = reverse_lazy('contact')
    template_name = "public/views/contact.html"

    def form_valid(self, form, **kwargs):
        # Data collection
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        object_url = get_admin_url
        site_url = self.request.build_absolute_uri(reverse('home'))

        admin_subject = _("IsTech: Request of consultancy - Action required")
        admin_text_content = _(
            f"A new application for a consultancy is registered\n\n"
            f"I hope this message finds you well.\n"
            f"I would like to inform you that a new consultancy application for isTech has been submitted by a customer and requires your attention.\n\n"
            f"Application Details:\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone/Mobile: {phone}\n"
            f"Message: {message}\n\n"
            f"You can check the details of the request <a href='{object_url}' target='_blank'>in here</a>.\n\n"
            f"Once the application is approved, please follow the procedures necessary to grant the client request.\n\n"
            f"Thank you for your prompt attention to this request.\n\n"
            f"Kind regards,\n"
            f"IsTech"
        )
        admin_html_content = get_template('public/email/admin.html').render({
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
            'object_url': object_url,
            'site_url': site_url,
        })
        admin_msg = EmailMultiAlternatives(admin_subject, admin_text_content, from_email, admin_emails, headers={
            'Reply-To': 'support@istech.tn',
            'Return-Path': 'support@istech.tn',
            'X-Sender': from_email,
        })
        admin_msg.attach_alternative(admin_html_content, "text/html")
        admin_msg.send()

        client_subject = _("IsTech: Request for IT Consultancy Services - Confirmation")
        client_to_email = [email]
        client_text_content = _(
            f"Confirmation of Request for IT Consultancy Services\n\n"
            f"Thank you for your interest in IsTech's IT consultancy services.\n"
            f"We are excited to begin our collaboration and provide you with the best possible solutions for your business needs.\n\n"
            f"Application Details:\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone/Mobile: {phone}\n"
            f"Message: {message}\n\n"
            f"This email is to confirm that we have received your request for IT consultancy services. Our team is currently reviewing your requirements and will reach out to you shortly to discuss the next steps.\n"
            f"In the meantime, please feel free to browse through our website to learn more about our comprehensive range of services and solutions. Should you have any immediate questions or concerns, please don't hesitate to contact us.\n"
            f"We appreciate the opportunity to work with you and look forward to the possibility of building a successful partnership.\n\n"
            f"Kind regards,\n"
            f"IsTech"
        )
        client_html_content = get_template('public/email/client.html').render({
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
            'site_url': site_url,
        })
        client_msg = EmailMultiAlternatives(client_subject, client_text_content, from_email, client_to_email, headers={
            'Reply-To': 'support@istech.tn',
            'Return-Path': 'support@istech.tn',
            'X-Sender': from_email,
        })
        client_msg.attach_alternative(client_html_content, "text/html")
        client_msg.send()

        return super().form_valid(form)
