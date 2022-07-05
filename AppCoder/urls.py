from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio,name= 'Inicio'),
    path('autos/',autos,name= 'Autos'),
    path('clientes/',clientes,name= 'Clientes'),
    path('empleados/',empleados,name= 'Empleados'),
    path('about/',about, name='About'),
    path( 'vacio/',vacio,name='Vacio'),
    
    path('autosFormulario/',autosFormulario,name='AutosFormulario'),
    path('clienteFormulario/',clienteFormulario,name='ClienteFormulario'),
    path('empleadoFormulario/',empleadoFormulario,name='EmpleadoFormulario'),

    path('listaAutos/', listaAutos , name= 'LeerAutos'),
    path('listaEmpleados/', listaEmpleados , name= 'LeerEmpleados'),
    path('listaClientes/', listaClientes , name= 'LeerClientes'),

    path('buscaAutos/',buscaAutos, name='BuscadorAutos'),
    path('buscar/',buscar),

    path( 'buscaClientes/',buscaClientes, name = 'BuscadorClientes'),
    path('buscar_c/', buscar_c),

    path( 'buscaEmpleados/',buscaEmpleados, name = 'BuscadorEmpleados'),
    path('buscar_e/', buscar_e ),

    path('pages/', AutoList.as_view(), name = 'List'),
    path('autoDetalle/<pk>/', AutoDetalle.as_view(), name = 'Detail'),
    path('autoDelete/<pk>/', AutoDelete.as_view(), name = 'Delete'),
    path('autoEdit/<pk>/', AutoUpdate.as_view(), name = 'Edit'),
    path('autoCreate', AutoCreacion.as_view(), name = 'Create'),

    path('cliente/list/', ClienteList.as_view(), name = 'List_c'),
    path('clienteDetalle/<pk>/', ClienteDetalle.as_view(), name = 'Detail_c'),
    path('clienteDelete/<pk>/', ClienteDelete.as_view(), name = 'Delete_c'),
    path('clienteEdit/<pk>/', ClienteUpdate.as_view(), name = 'Edit_c'),
    path('clienteCreate', ClienteCreacion.as_view(), name = 'Create_c'),
    

    path('empleado/list/', EmpleadoList.as_view(), name = 'List_e'),
    path('empleadoDetalle/<pk>/', EmpleadoDetalle.as_view(), name = 'Detail_e'),
    path('empleadoDelete/<pk>/', EmpleadoDelete.as_view(), name = 'Delete_e'),
    path('empleadoEdit/<pk>/', EmpleadoUpdate.as_view(), name = 'Edit_e'),
    path('empleadoCreate', EmpleadoCreacion.as_view(), name = 'Create_e'),
    
    
    
    # path(r'^(?p<pk>\d+)$', AutoDetalle.as_view(), name = 'Detail'), 
    # path(r'^borrar/(?p<pk>\d+)$', AutoDelete.as_view(), name = 'Delete'), 


    path('login/', login_request, name = 'Login'),
    path('register/', register, name = 'Registro'),
    
    path('logout/', LogoutView.as_view(template_name = 'AppCoco/logout.html'), name = 'Logout'),
    


]