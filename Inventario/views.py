from django.shortcuts import render,redirect
from .models import Inventario

# Create method
def create(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        tipo = request.POST['tipo']
        serial = request.POST['serial']
        valorcompra = request.POST['valorcompra']
        fechadecompra = request.POST['fechadecompra']
        estado = request.POST['estado']
        area = request.POST['area']
        persona = request.POST['persona']
        id = None
        obj = Inventario(id,nombre,descripcion,tipo,serial,valorcompra,fechadecompra,estado,area, persona)
        obj.save()
        return redirect('/')
   
# Read method   
def read(request):
    try:
        obj = Inventario.objects.all()
    except Inventario.DoesNotExist:
        obj = None
    return render(request,'index.html',{'key':obj})

# Update method
def update(request,id):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        tipo = request.POST['tipo']
        serial = request.POST['serial']
        valorcompra = request.POST['valorcompra']
        fechadecompra = request.POST['fechadecompra']
        estado = request.POST['estado']
        area = request.POST['area']
        persona = request.POST['persona']
        obj1 = Inventario.objects.get(id=id)
        obj1.nombre = nombre
        obj1.descripcion = descripcion
        obj1.tipo = tipo
        obj1.serial = serial
        obj1.fechadecompra = fechadecompra
        obj1.valorcompra = valorcompra
        obj1.area = area
        obj1.persona = persona
        obj1.estado = estado
        obj1.save()
        return redirect('/')
    else:
        try:
            obj = Inventario.objects.get(id=id)
        except Inventario.DoesNotExist:
            obj = None

        return render(request,'edit.html',{'key':obj})

# Delete method
def delete(request,id):
    try:
        obj = Inventario.objects.get(id=id)
    except Inventario.DoesNotExist:
        obj = None
    
    obj.delete()
    return redirect('/')
