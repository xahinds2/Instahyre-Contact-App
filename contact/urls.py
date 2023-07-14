from contact import views
from django.urls import path

urlpatterns = [
    path('my_contacts/', views.my_contacts, name='my_contacts'),
    path('search_contacts/', views.search_contacts, name='search_contacts'),
    path('my_contacts/search_contacts/', views.search_contacts, name='search_contacts'),
    path('populate/', views.populate, name='populate'),
    path('populate/<int:qty>', views.populate, name='populate'),
    path('spam/<int:cid>', views.spam, name='spam'),
]
