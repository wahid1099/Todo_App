
from django.urls import path

from .views import index, about, deleteTodo

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('delete-Todo/<int:id>/', deleteTodo, name="deleteTodo")
]
