import os

from django.shortcuts import render
from .forms import *


# Create your views here.

def upload_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            return render(request, 'blur_app/upload.html', {'form': form, 'img': img})
    else:
        form = UploadImageForm()

    if request.GET.get('delete-button'):
        pk = request.GET.get('delete-button')
        print(pk)
        uploaded_file = UploadedFile.objects.get(id=pk)
        uploaded_file.delete_image(uploaded_file, pk)
        form = UploadImageForm()

    return render(request, 'blur_app/upload.html', {'form': form})
