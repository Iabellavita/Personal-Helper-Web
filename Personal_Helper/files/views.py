from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .models import Files
from django.http import FileResponse
import os


@login_required(login_url='home')
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            filename = request.FILES['uploadfile'].name
            print(filename)
            form.instance.user = request.user
            form.save()

            files = Files.objects.filter(user=request.user)
            form = UploadFileForm()
            return render(request, "files/index.html", {"files": files, "form": form, "filename": filename})

    else:
        form = UploadFileForm()
        files = Files.objects.filter(user=request.user)
        return render(request, "files/index.html", {"files": files, "form": form})


@login_required(login_url='home')
def delete_file(request, file_id):
    file = Files.objects.get(pk=file_id)
    file.delete()
    os.remove(f'./media/{file.uploadfile}')

    return redirect(upload_file)


@login_required(login_url='home')
def download_file(request, file_id):
    file = Files.objects.get(pk=file_id)

    filepath = f'./media/{file.uploadfile}'
    filename = filepath.split('/')[6]

    path = open(filepath, 'rb')
    return FileResponse(path, as_attachment=True, filename=filename,
                        content_type=f'application/{filename.split(".")[1]}')
