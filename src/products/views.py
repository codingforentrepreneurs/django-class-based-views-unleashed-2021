from django.views.generic import ListView, DetailView

from .mixins import TemplateTitleMixin
from .models import Product, DigitalProduct


class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name = 'products/product_list.html'
    title = 'Digital Downloads'


class ProductListView(TemplateTitleMixin, ListView):
    model = Product
    title = 'Products'


class ProductDetailView(DetailView):
    model = Product