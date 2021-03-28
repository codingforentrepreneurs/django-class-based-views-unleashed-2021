from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, RedirectView, View
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator

from .mixins import TemplateTitleMixin
from .models import Product, DigitalProduct


class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        # obj.get_absolute_url()
        return f'/products/{obj.slug}/'


class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        print(self.request.path, self.request.build_absolute_uri())
        return f'/products/{url_params.get("slug")}/'


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



class ProductMixinDetailView(MultipleObjectMixin, View):
    queryset = Product.objects.all() # .filter(pk__gte=2)

    # def get_queryset(self):
    #     return Product.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        print(self.kwargs)
        pk = kwargs.get('pk')
        self.object_list = self.get_queryset().filter(pk=pk)
        qs = self.object_list
        if not qs.exists():
            raise Http404('this was not found')
        obj = qs.get()
        context = self.get_context_data()
        context['object'] = obj
        print(context)
        app_label = self.object_list.model._meta.app_label
        model_name = self.object_list.model._meta.model_name
        template = f"{app_label}/{model_name}_detail.html"
        return render(request, template, context)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


# class MyLoginRequiredMixin():
#     @method_decorator(login_required)
#     @method_decorator(cache_page)
#     @method_decorator(permission_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch( *args, **kwargs)


class MyProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    
    # def get_object(self):
    #     url_kwarg_id = self.kwargs.get("id")
    #     qs = self.get_queryset().filter(id=url_kwarg_id)
    #     if not qs.exists():
    #         raise Http404('Product not found')
    #     return qs.get()

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     print(self.kwargs)
    #     return context