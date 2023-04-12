from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book
from django.db.models import Q


class HomeView(ListView):
    queryset = Book.objects.order_by("id")
    template_name = "home.html"
    context_object_name = "books"


class ProductView(DetailView):
    model = Book
    template_name = "books/product.html"


def category(request, pk):

    results = Book.objects.filter(Q(category_id=pk))
    context = {'books': results}
    return render(request, 'books/category.html', context)



def search(request):
    query = request.GET.get('q')
    results = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    context = {'results': results, 'query': query}
    return render(request, 'books/search.html', context)



def my_custom_404_view(request, exception):
    return render(request, '404.html', {})
