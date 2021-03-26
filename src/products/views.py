from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    # app_name = products
    # model = product
    # view_name = list
    # template_name = <app_name>/<model>_<view_name>.html
    model = Product
    # template_name = 'myproducts.html'
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        qs = context['object_list']
        # context['object_list'] = Product.objects.none()
        context['title'] = "My Title"
        return context


class ProductDetailView(DetailView):
    model = Product