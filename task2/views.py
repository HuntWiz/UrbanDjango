from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    template_name = 'obj_index.html'