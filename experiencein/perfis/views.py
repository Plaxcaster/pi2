# experiencein/perfis/views.py

from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

# importando redirect
from django.shortcuts import redirect

# código comentado

# modificando a função convidar

def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)

    # realizando redirecionamento
    return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1) 