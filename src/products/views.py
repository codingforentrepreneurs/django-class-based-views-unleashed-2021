from django.views.generic import ListView, DetailView, View
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render

from .mixins import TemplateTitleMixin
from .models import Product, DigitalProduct


class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name = 'products/product_list.html'
    title = 'Digital Downloads'




class ProductObjectMixinListView(MultipleObjectMixin, View):
    queryset = Product.objects.filter(pk__gte=2)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        app_label = self.object_list.model._meta.app_label
        model_name = self.object_list.model._meta.model_name
        template = f"{app_label}/{model_name}_list.html"
        return render(request, template, context)


class ProductListView(TemplateTitleMixin, ListView):
    model = Product
    title = 'Products'


class ProductDetailView(DetailView):
    model = Product