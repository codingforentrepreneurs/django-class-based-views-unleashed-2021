from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    # app_name = products
    # model = product
    # view_name = list
    # template_name = <app_name>/<model>_<view_name>.html
    model = Product
    # template_name = 'myproducts.html'


class ProductDetailView(DetailView):
    model = Product