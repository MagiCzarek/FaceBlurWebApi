from django.urls import path
from blur_app.views import *

app_name = 'blur_app'

urlpatterns = [
    path('upload/', upload_view, name='upload'),
]
