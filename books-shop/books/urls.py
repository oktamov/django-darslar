from django.urls import path

from books.views import HomeView, ProductView, index

urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('search/', index, name='book_search'),
    path('book/<int:pk>/', ProductView.as_view(), name="book")
]
