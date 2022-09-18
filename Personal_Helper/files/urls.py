from django.urls import path, include
from .views import *

urlpatterns = [
    path('files/', login_required(FilesByUser.as_view(), login_url='home'), name='files'),
    path('download_file/<int:file_id>/', download_file, name='download_file'),
    path('delete_file/<int:file_id>/', delete_file, name='delete_file'),
    path('add_file/', upload_file, name='upload_file'),
    path('search_files/', login_required(Search.as_view(), login_url='home'), name='search_file'),
    path('files/images', login_required(ImagesFiles.as_view(), login_url='home'), name='image_files'),
    path('files/docs', login_required(DocsFiles.as_view(), login_url='home'), name='docs_files'),
    path('files/pdf', login_required(PDFFiles.as_view(), login_url='home'), name='pdf_files'),
]
