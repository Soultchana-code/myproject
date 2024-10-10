from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog_index"),
    # Ajoutez d'autres motifs d'URL ici si nécessaire
]
