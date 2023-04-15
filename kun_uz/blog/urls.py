from django.urls import path

from .views import HomeView, NewsDetailView, CategoryView, category, search

urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('news/<str:slug>/', NewsDetailView.as_view(), name="one_news"),
    path('category/<int:pk>/', category, name='category'),
    path('search/', search, name='search'),
]