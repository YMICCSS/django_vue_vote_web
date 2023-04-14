from django.urls import path
from . import views
from .views import ItemListCreateView, ItemRetrieveDeleteView

urlpatterns = [
    path('items/', ItemListCreateView.as_view()),
    path('items/<int:pk>/', ItemRetrieveDeleteView.as_view()),
]