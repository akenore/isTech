from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomeView(TemplateView):
    template_name = "public/views/home.html"


class ServiceView(TemplateView):
    template_name = "public/views/service.html"


class WorkView(TemplateView):
    template_name = "public/views/work.html"


class ContactView(TemplateView):
    template_name = "public/views/contact.html"
