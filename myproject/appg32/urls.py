from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload'),  # Correctly reference 'upload_file'
]
