from django.urls import path
from .views import MyFeed, SelectFeed

urlpatterns = [
    path("", MyFeed.as_view()),
    path("/<str:username>", SelectFeed.as_view())
]
