from contact import views
from django.urls import path

urlpatterns = [
    path('contacts/', views.dashboard, name='dashboard'),
]
