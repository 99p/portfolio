from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = "ponponboy's portfolio"
        return ctx

index = Index.as_view()
