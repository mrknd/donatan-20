from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('inquiry_short/', views.inquiry_short, name='inquiry_short'),
]