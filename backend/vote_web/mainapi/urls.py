from django.urls import path
from .views import ItemListCreateView, ItemRetrieveDeleteView,VoteAPIView

urlpatterns = [
    path('items/', ItemListCreateView.as_view()),
    path('items/<int:pk>/', ItemRetrieveDeleteView.as_view()),
    path('votes/', VoteAPIView.as_view()),
]

