from contact import views
from django.urls import path

urlpatterns = [
    path('contacts/', views.dashboard, name='dashboard'),
    path('search_contacts/', views.search_contacts, name='search_contacts'),
    path('contacts/search_contacts/', views.search_contacts, name='search_contacts'),
]
