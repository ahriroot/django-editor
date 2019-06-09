from django.urls import path
from . import views
app_name = 'ckeditor'

urlpatterns = [
    path('upload', views.upload, name='upload'),
]
