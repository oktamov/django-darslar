from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book
from django.db.models import Q


class HomeView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "home.html"
    context_object_name = "books"


class ProductView(DetailView):
    model = Book
    template_name = "product.html"

# def nom(requests, pk):
#     print(requests)
#     book = Book.objects.all().filter(id=pk)
#     return render(requests, 'product.html', {'books': book})


def index(request):
    search_post = request.GET.get('q')

    books = Book.objects.filter(search_post)

    return render(request, 'book_search.html', {'books': books})

