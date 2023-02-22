from django.urls import path
from .views import MyFeed

urlpatterns = [
    path("", MyFeed.as_view())
]
