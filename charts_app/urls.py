# charts_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cancer_types_view, name='cancer-types'),
    path('', views.censoring_data_view, name='censoring-data'),
]
