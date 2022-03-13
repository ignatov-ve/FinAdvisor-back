from django.urls import path

from . import views

urlpatterns = [
    path('api/okveds/', views.get_all_okveds),
    path('api/okveds/<str:industry>/', views.get_okveds_by_industry),
    path('api/industries/', views.get_all_industries),
    path('api/regions/', views.get_all_regions),
    path('api/prediction/', views.get_prediction),
]
