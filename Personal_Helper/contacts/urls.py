from django.urls import path

from .views import *

urlpatterns = [
    path('create-contact/', create_contact, name='create_contact'),
    path('contacts/', ContactByUser.as_view(), name='contact_list'),
    path('contact/<int:pk>', user_contact, name='contact'),
    path('search/', Search.as_view(), name='search_contact'),
]
