from django.urls import path
from . import views
from .views import ItemListCreateView, ItemRetrieveDeleteView
from .views import vote
urlpatterns = [
    path('items/', ItemListCreateView.as_view()),
    path('items/<int:pk>/', ItemRetrieveDeleteView.as_view()),
    path('votes/', vote),
]

