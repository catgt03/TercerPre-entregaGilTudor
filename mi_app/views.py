from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ClienteForm, ProductoForm


def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    
    # Cargar el contenido de la plantilla desde un archivo
    with open('mi_app/index.html', 'r') as template_file:
        template = Template(template_file.read())
    
    context = Context({'categorias': categorias, 'productos': productos, 'clientes': clientes})
    
    # Renderizar la plantilla con el contexto
    rendered_template = template.render(context)
    
    return HttpResponse(rendered_template)

def agregar_categoria(request):
    if request.method == 'POST':
        # Procesar el formulario si se envía
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después de agregar una categoría
    else:
        form = CategoriaForm()
    
    # Cargar el contenido de la plantilla desde un archivo
    with open('mi_app/agregar_categoria.html', 'r') as template_file:
        template = Template(template_file.read())
    
    context = Context({'form': form})
    
    # Renderizar la plantilla con el contexto
    rendered_template = template.render(context)
    
    return HttpResponse(rendered_template)

def agregar_producto(request):
    if request.method == 'POST':
        # Procesar el formulario si se envía
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después de agregar un producto
    else:
        form = ProductoForm()
    
    # Cargar el contenido de la plantilla desde un archivo
    with open('mi_app/agregar_producto.html', 'r') as template_file:
        template = Template(template_file.read())
    
    context = Context({'form': form})
    
    # Renderizar la plantilla con el contexto
    rendered_template = template.render(context)
    
    return HttpResponse(rendered_template)

def agregar_cliente(request):
    if request.method == 'POST':
        # Procesar el formulario si se envía
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después de agregar un cliente
    else:
        form = ClienteForm()
    
    # Cargar el contenido de la plantilla desde un archivo
    with open('mi_app/agregar_cliente.html', 'r') as template_file:
        template = Template(template_file.read())
    
    context = Context({'form': form})
    
    # Renderizar la plantilla con el contexto
    rendered_template = template.render(context)
    
    return HttpResponse(rendered_template)




