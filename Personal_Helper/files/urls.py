from django.urls import path, include
from .views import *

urlpatterns = [
    path('files', FilesByUser.as_view(), name='files'),
    path('download_file/<int:file_id>/', download_file, name='download_file'),
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
    path('add_file/', upload_file, name='upload_file'),
    path('search/', Search.as_view(), name='search_file'),
    path('image_files/', ImagesFiles.as_view(), name='image_files'),
    path('docs_files/', DocsFiles.as_view(), name='docs_files'),
    path('pdf_files/', PDFFiles.as_view(), name='pdf_files'),
]
