from django.views.generic import View, ListView
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['GET'])
def product_list_view(request):
    # qs = Product.objects.all()
    if request.method == 'POST':
        print(request.POST) # DjangoModelForm
    print(request.method == 'POST')
    return render(request, 'template', {})

class ProductHomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'template', {})
    
    def post(self, request, *args, **kwargs):
        print(request.POST) # DjangoModelForm
        return 


class ProductListView(ListView):
    queryset = Product.objects.all()

class BlogPostsListView(ListView):
    queryset = Post.objects.all()

class UsersListView(ListView):
    queryset = User.objects.all()