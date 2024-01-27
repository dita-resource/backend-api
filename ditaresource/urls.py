from django.urls import path

from .views import ClientDetailView

urlpatterns = [
    path('clients/', ClientDetailView.as_view()),
]
