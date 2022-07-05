
from dataclasses import fields
from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.forms import *
from AppCoder.models import Auto, Cliente, Empleado

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView ,DeleteView

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    
def autos(request):
    
    return render(request,'AppCoder/autos.html')

def empleados(request):
    return render(request,'AppCoder/empleados.html')
    
def clientes(request):
    return render(request,'AppCoder/clientes.html')

def about(request):
    return render(request,'AppCoder/about.html')

def vacio(request):
    return render(request, 'AppCoder/vacio.html')

@login_required
def autosFormulario(request):
    
    
    if request.method == 'POST':

        mi_formulario = AutosFormulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            auto = Auto(marca = informacion["marca"], modelo = informacion["modelo"], motor = informacion["motor"])
            auto.save()

            return render(request,'AppCoco/inicio.html')
    else:
        mi_formulario =AutosFormulario()
        return render(request, 'AppCoder/autosFormulario.html',{"mi_formulario": mi_formulario})


@login_required
def clienteFormulario(request):

    if request.method == 'POST':

        mi_formulario = ClienteFormulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            cliente = Cliente(nombre = informacion["nombre"],apellido = informacion["apellido"],email = informacion["email"])
            cliente.save()

            return render(request,'AppCoder/inicio.html')
    else:
        mi_formulario =ClienteFormulario()
        return render(request, 'AppCoder/clienteFormulario.html',{"mi_formulario": mi_formulario})

@login_required
def empleadoFormulario(request):

    if request.method == 'POST':

        mi_formulario = EmpleadoFormulario(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            empleado = Empleado(nombre = informacion["nombre"],apellido = informacion["apellido"],email = informacion["email"],encargo = informacion["encargo"])
            empleado.save()

            return render(request,'AppCoder/inicio.html')
    else:
        mi_formulario =EmpleadoFormulario()
        return render(request, 'AppCoder/empleadoFormulario.html',{"mi_formulario": mi_formulario})

def buscaAutos(request):
    return render(request,'AppCoder/buscaAutos.html')

def buscar(request):
    if request.GET['marca']:

        #respuesta = f"Estoy buscando autos marca {request.GET['marca']}"

        marca= request.GET['marca']
        autos = Auto.objects.filter(marca=marca)

        return render(request,'AppCoder/resultadosBusqueda.html',{'autos': autos , "marca":marca})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)



def buscaClientes(request):
    return render(request,'AppCoder/buscaClientes.html')

def buscar_c(request):
    if request.GET['apellido']:

        #respuesta = f"Estoy buscando autos marca {request.GET['marca']}"

        apellido= request.GET['apellido']
        clientes = Cliente.objects.filter(apellido=apellido)

        return render(request,'AppCoder/resultadosBusqueda_c.html',{'clientes': clientes , "apellido": apellido})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)



def buscaEmpleados(request):
    return render(request,'AppCoder/buscaEmpleados.html')

def buscar_e(request):
    if request.GET['encargo']:

        #respuesta = f"Estoy buscando autos marca {request.GET['marca']}"

        encargo= request.GET['encargo']
        empleados = Empleado.objects.filter(encargo=encargo)

        return render(request,'AppCoder/resultadosBusqueda_e.html',{'empleados': empleados , "encargo": encargo})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def listaAutos(request):

    autos = Auto.objects.all()

    contexto = {'autos':autos}

    return render(request, 'AppCoder/listaAutos.html',contexto)

def listaEmpleados(request):

    empleados = Empleado.objects.all()

    contexto = {'empleados':empleados}

    return render(request, 'AppCoder/listaEmpleados.html',contexto)

def listaClientes(request):

    clientes = Cliente.objects.all()

    contexto = {'clientes':clientes}

    return render(request, 'AppCoder/listaClientes.html',contexto)



def login_request(request):

    if request.method == 'POST':
        
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():

            data = form.cleaned_data

            

            user = authenticate(username = data["username"] , password = data["password"])


            if user is not True:
            
                login(request,user)

                return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido {user.get_username()}'} )
            
            else:
                return render(request,'AppCoder/inicio.html', {'mensaje':'Error, Datos incorrectos'})

        else:
            return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, Formulario erroneo'})
    else:
        form = AuthenticationForm()

    return render(request, 'AppCoder/login.html',{'form':form})



def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render(request, 'AppCoder/inicio.html', {'mensaje':'Usuario Creado Exitosamente'})
        else:
            return render(request, 'AppCoder/inicio.html', {'mensaje':'Form erroneo, las contraseñas no coinciden'})
    else:
        form = UserCreationForm()

        return render(request, 'AppCoder/registro.html', {'form' : form} )


# def editarAuto(request, auto_marca):
#     auto = Auto.objects.get(marca = auto_marca)


#     if request.method == 'POST':
#         mi_formulario = AutosFormulario(request.POST)


#         print(mi_formulario)
        
#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
            
#             auto.marca = informacion['marca']
#             auto.modelo = informacion['modelo']
#             auto.motor = informacion['motor']

#             auto.save()
#             return render(request,'AppCoco/inicio.html')
#     else:
#         mi_formulario = AutosFormulario(initial={'marca': auto.marca, 'modelo':auto.modelo, 'motor':auto.motor  })

#     return render(request, 'AppCoco/editarAuto.html', {'mi_formulario': mi_formulario,'auto_marca': auto_marca})




class AutoList(ListView):
    
    model = Auto
    template_name = 'AppCoder/autoList.html'

class AutoDetalle(DetailView):
    
    model = Auto
    template_name = 'AppCoder/autoDetalle.html'

class AutoUpdate(LoginRequiredMixin,UpdateView):
    model = Auto
    success_url = '/AppCoder/pages/'
    fields = ['marca','modelo','motor']
    template_name = 'AppCoder/auto_form.html'

class AutoDelete(LoginRequiredMixin , DeleteView):
    model = Auto
    success_url = '/AppCoder/pages/'
    template_name = 'AppCoder/auto_confirm_delete.html'

class AutoCreacion(CreateView):
    model = Auto
    success_url = '/AppCoder/pages/'
    fields = ['marca','modelo','motor']
    template_name = 'AppCoder/autos.html'




class ClienteList(ListView):
    
    model = Cliente
    template_name = 'AppCoder/clienteList.html'

class ClienteDetalle(DetailView):
    
    model = Cliente
    template_name = 'AppCoder/clienteDetalle.html'

class  ClienteUpdate(LoginRequiredMixin,UpdateView):
    model = Cliente
    success_url = '/AppCoder/cliente/list/'
    fields = ['nombre','apellido','email']
    template_name = 'AppCoder/cliente_form.html'

class ClienteDelete(LoginRequiredMixin , DeleteView):
    model = Cliente
    success_url = '/AppCoder/cliente/list'
    template_name = 'AppCoder/cliente_confirm_delete.html'

class ClienteCreacion(CreateView):
    model = Cliente
    success_url = '/AppCoder/cliente/list/'
    fields = ['nombre','apellido','email']
    template_name = 'AppCoder/clientes.html'



class EmpleadoList(ListView):
    
    model = Empleado
    template_name = 'AppCoder/empleadoList.html'

class EmpleadoDetalle(DetailView):
    
    model = Empleado
    template_name = 'AppCoder/empleadoDetalle.html'

class  EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    success_url = '/AppCoder/empleado/list/'
    fields = ['nombre','apellido','email','encargo']
    template_name = 'AppCoder/empleado_form.html'

class EmpleadoDelete(LoginRequiredMixin , DeleteView):
    model = Empleado
    success_url = '/AppCoder/empleado/list'
    template_name = 'AppCoder/empleado_confirm_delete.html'

class EmpleadoCreacion(CreateView):
    model = Empleado
    success_url = '/AppCoder/empleado/list/'
    fields = ['nombre','apellido','email','encargo']
    template_name = 'AppCoder/empleados.html'