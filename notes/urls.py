from django.urls import path
from .views import *

urlpatterns = [
    path('create-note/', create_note, name='create_note'),
    path('create-tag/', create_tag, name='create_tag'),
    path('note/<int:pk>', user_note, name='note'),
    path('notes/', login_required(NoteByUser.as_view(), login_url='home'), name='notes_list'),
    path('search-note/', login_required(Search.as_view(), login_url='home'), name='search_notes'),
]