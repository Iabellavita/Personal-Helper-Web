from django.urls import path, include
from .views import *

urlpatterns = [
    path('file-storage', upload_file, name='uploadFile'),
    path('download_file/<int:file_id>/', download_file, name='download_file'),
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
]
