from django.urls import path
from . import views
app_name = 'wangeditor'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
]
