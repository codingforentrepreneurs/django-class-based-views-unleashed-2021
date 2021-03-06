from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
        CreateView, 
        ListView, 
        DetailView, 
        DeleteView,
        RedirectView, 
        UpdateView,
        View
)
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator

from .forms import ProductModelForm
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
      def get_queryset(self):
        return Product.objects.filter(user=self.request.user)



class MyProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm
    template_name = 'forms.html'
    # success_url = '/products'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MyProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm
    template_name_suffix = '_detail'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.object.get_edit_url()


class MyProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'forms-delete.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return "/products/"




def product_update_view(request, slug, *args, **kwargs):
    obj = Product.objects.get(slug=slug)
    form = ProductModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "object": obj,
        "form": form,
    }
    return render(request, "forms.html", context)

class MyProductBaseFormView(LoginRequiredMixin, ModelFormMixin, View):
    form_class = ProductModelForm
    template_name = 'forms.html'
    # success_url = '/products'

    def get_form_kwargs(self):
        return {"instance": Product.objects.first()}
    
    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)