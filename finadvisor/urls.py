from django.urls import path

from . import views

urlpatterns = [
    path('api/okved/', views.OkvedListCreate.as_view()),
]
