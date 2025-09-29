from django.urls import path
from galeria.views import index, image

urlpatterns = [
    path('', index),
    path('imagem/', image, name='image'),
]