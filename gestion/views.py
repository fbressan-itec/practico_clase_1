from django.shortcuts import render, redirect, get_object_or_404
from .models import Spot
from .forms import SpotForm

# Create your views here.

def home(request):
    return render (request, 'home.html')


def list_cocheras(request):
    # Traemos todos los spots ordenados por número
    cocheras = Spot.objects.all().order_by('numero')
    return render(request, 'gestion/main.html', {'cocheras': cocheras})

# crear cochera
def crear_cochera(request):
    if request.method == "POST":
        form = SpotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('list_cocheras')
    else: 
        form = SpotForm()
    
    return render(request, 'gestion/form.html', {'form':form, 'titulo_form':'Completa los datos del formulario de crear cochera'}) #AGREGAAAAAAAAAAR RUTAAAAAAAAAAAAAAAAA

#editar cochera
def editar_cochera (request, id):

    spot = get_object_or_404(Spot, id=id)

    if request.method == "POST":
        form = SpotForm(request.POST, instance=spot)
        if form.is_valid():
            form.save()
            return redirect ('list_cocheras')

    else:
        form = SpotForm(instance=spot)

    return render(request, 'gestion/form.html', {'form':form, 'titulo_form':'Completa los datos del formulario de editar cochera'}) #AGREGAAAAAAAAAAR RUTAAAAAAAAAAAAAAAAA

#Eliminar o cambiar estado
def liberar_cochera (request, id):
    spot=get_object_or_404(Spot, id=id)
    if request.method == "POST":
        #cambiar estado de libre
        spot.estado = 'LIBRE'
        spot.vehiculo = None
        spot.responsable = None
        spot.ingreso = None
        spot.save()
        return redirect ("list_cocheras")

    return render(request, 'gestion/main.html', {"spot":spot}) #AGREGAAAAAAAAAAR RUTAAAAAAAAAAAAAAAAA

def eliminar_cochera (request, id):
    spot=get_object_or_404(Spot, id=id)
    if request.method == "POST":
        #borrado total
        spot.delete()

        #borrado logico
        #spot.is_active = False
        #spot.save()

        return redirect ("list_cocheras")

    return render(request, 'gestion/confirmar_eliminar.html', {"spot":spot, 'titulo_form':'Esta seguro que desea eliminar cochera?'}) #AGREGAAAAAAAAAAR RUTAAAAAAAAAAAAAAAAA

