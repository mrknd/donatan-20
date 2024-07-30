from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:stroller_slug>/', views.stroller_detail, name='stroller_detail'),
]