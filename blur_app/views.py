from django.shortcuts import render
from .forms import *


# Create your views here.

def upload_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img = form.instance
            return render(request, 'blur_app/upload.html', {'form': form, 'img': img})
    else:
        form = UploadImageForm()
    return render(request, 'blur_app/upload.html', {'form': form})

    context = {}
    return render(request, 'blur_app/upload.html', context)
