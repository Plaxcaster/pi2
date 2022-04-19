# editando o arquivo experiencein/perfis/views.py
# experiencein/perfis/views.py 
from django.shortcuts import render 

def index(request): 
    return render(request, 'index.html')