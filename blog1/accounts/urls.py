from django.urls import path, include
from .views import SignUpView

appname = "accounts"
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
