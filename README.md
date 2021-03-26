[![Django CBV Unleashed Logo](https://static.codingforentrepreneurs.com/media/projects/django-class-based-views-unleashed/images/share/Django_Class_Based_Views_Unleashed_shar.jpg)](https://www.codingforentrepreneurs.com/projects/django-class-based-views-unleashed)

# [Django Class Based Views Unleahsed](https://www.codingforentrepreneurs.com/projects/django-class-based-views-unleashed)

Django Class Based Views (*CBVs*) are an important part of using Django effectively.  *CBVs* help us eliminate redundant code across our entire application and stay DRY while using CRUD and CRUD-like views. 

Here's a basic example:

```python
def my_home_view(request):
      return render(request, 'home.html', {})
```
Becomes

```python
class MyHomeView(View):
     def get(self, request, *args, **kwargs):
          return render(request, 'home.html', {})


my_home_view = MyHomeView.as_view()
```

This, of course, isn't ground breaking. How about a detail view? or a List view?


```python
class SomeModelListView(ListView):
     model = SomeModel
```

```python
class SomeModelDetailView(DetailView):
     model = SomeModel
```

These two classes provide us a default template, a default lookup (for a QuerySet or object lookup), and  default template context. These defaults can be reused for *any* model in your project. 

This series will explore all of above and much more.

#### Recommend Experience
- Any [Try Django](https://cfe.sh/topics/try-django) series


#### Watch the tutorial [here](https://www.codingforentrepreneurs.com/projects/django-class-based-views-unleashed)
