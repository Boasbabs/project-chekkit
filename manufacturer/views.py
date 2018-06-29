from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, template_name="manufacturer/index.html", context={})

# def generate_id(request):
#     return render(request, template_name="manufacturer/generate-id.html", context={})


class GenerateIdView(TemplateView):
    template_name = "manufacturer/generate-id.html"
