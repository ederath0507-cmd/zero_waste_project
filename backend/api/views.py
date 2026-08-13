from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alimento
from .serializers import AlimentoSerializer

# --- VISTAS DE PÁGINAS HTML ---
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'informacion.html')

def profile_view(request):
    return render(request, 'perfil.html')

def settings_view(request):
    return render(request, 'configuracion.html')

def create_food(request):
    return render(request, 'publicar.html')

# --- ENDPOINT API REST PARA ALIMENTOS ---
@api_view(['GET', 'POST'])
def lista_alimentos(request):
    if request.method == 'GET':
        categoria = request.query_params.get('categoria', None)
        if categoria and categoria != 'Todos':
            alimentos = Alimento.objects.filter(categoria__iexact=categoria)
        else:
            alimentos = Alimento.objects.all().order_by('-creado_en')
        
        serializer = AlimentoSerializer(alimentos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlimentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)