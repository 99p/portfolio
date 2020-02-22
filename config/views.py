from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'startbootstrap-grayscale/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = "ponponboy's Portfolio"
        return ctx
