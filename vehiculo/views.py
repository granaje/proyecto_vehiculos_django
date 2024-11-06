from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import permission_required


@permission_required('vehiculo.add_vehiculomodel', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add.html', {'form': form})


def index(request):
    return render(request, 'vehiculo/index.html')

@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()  # Recupera todos los vehículos
    return render(request, 'vehiculo/list.html', {'vehiculos': vehiculos})
