from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Yangiliklar, Category


# Create your views here.
class HomeView(ListView):
    model = Yangiliklar
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["categories"] = Category.objects.order_by("id")
        return context


class NewsDetailView(DetailView):
    model = Yangiliklar
    template_name = "news/news.html"


class CategoryView(ListView):
    model = Yangiliklar
    template_name = 'news/category.html'


def category(request, pk):
    results = Yangiliklar.objects.filter(Q(category_id=pk))
    context = {'news': results}
    return render(request, 'news/category.html', context)


def search(request):
    query = request.GET.get('q')
    results = Yangiliklar.objects.filter(Q(title__icontains=query))
    context = {'news': results, 'query': query}
    return render(request, 'news/search.html', context)
