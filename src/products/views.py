from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render


def about_us_redirect_view(request):
    return HttpResponseRedirect("/about/")

def about_us_redirect_view(request):
    return HttpResponseRedirect("/about/")

def about_us_redirect_view(request):
    return HttpResponseRedirect("/about/")

def about_us_view(request):
    return render(request, "about.html", {})

class AboutUsView(TemplateView):
    template_name = 'about.html'