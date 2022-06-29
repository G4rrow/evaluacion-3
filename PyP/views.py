from django.shortcuts import render
from .models import Categoria
# Create your views here.
def home(request):

    Categorias=Categoria.objects.all()
    data = {}
    data["categorias"]=Categorias
    return render(request, 'home.html', data)



