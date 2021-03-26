from django.views.generic import View, TemplateView
from django.shortcuts import render

# Create your views here.
def about_us_view(request):
    return render(request, "about.html", {})

class AboutUsView(TemplateView):
    template_name = 'about.html'