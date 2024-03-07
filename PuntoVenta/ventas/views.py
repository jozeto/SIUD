from telnetlib import LOGOUT
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
"""
def ventas_vista(request):
    num_ventas = 156
    context ={
        'num_ventas': num_ventas
    }
    return render(request, 'ventas.html', context) # aca de coloca el template "el que finaliza en html"
"""
@login_required
def home(request):
    return render(request,"home.html")

@login_required
def login(request):
    return(render(request,'registration/login.html' ))
    
def exit(request):
    logout(request)
    return redirect('login')


#--------------------------CLIENTES -----------------------

def clientes_vista(request):
    if not request.user.is_staff:
        return render(request,"home.html")
    
    clientes = Cliente.objects.all()
    personas = Persona.objects.all()
    tiposcomercio = TipoComercio.objects.all()
    tiposcliente = TipoCliente.objects.all()
    form_personal = AgregarClienteForm()
    form_editar = EditarClienteForm()
    context ={
        'clientes' : clientes,
        'form_personal' : form_personal,
        'form_editar' : form_editar,

        'personas' : personas,
        'tiposcomercio' : tiposcomercio,
        'tiposcliente': tiposcliente
    }
    return render(request, 'clientes.html', context)

def agregar_Cliente_vista(request):
    if request.method == 'POST':
        form = AgregarClienteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    ciudad = Ciudad.objects.create(
                        ciudad=form.cleaned_data['ciudad'])

                    contacto = Contacto.objects.create(
                        telefono=form.cleaned_data['telefono'],
                        correo=form.cleaned_data['correo']
                        )
                    
                    direccion = Direccion.objects.create(
                        direccion=form.cleaned_data['direccion'],
                        barrio=form.cleaned_data['barrio'],
                        idciudad=ciudad,
                        )

                    persona = Persona.objects.create(
                        documentoidentidad=form.cleaned_data['documentoidentidad'],
                        primer_nombre=form.cleaned_data['primer_nombre'],
                        segundo_nombre=form.cleaned_data['segundo_nombre'],
                        primer_apellido=form.cleaned_data['primer_apellido'],
                        segundo_apellido=form.cleaned_data['segundo_apellido'],
                        genero=form.cleaned_data['genero'],
                        idcontacto=contacto,
                        iddireccion=direccion
                    )

                    cliente = Cliente.objects.create(
                        iddocumento=persona,
                        idtipo_comercio=form.cleaned_data['idtipo_comercio'],
                        idtipo_cliente=form.cleaned_data['idtipo_cliente'],
                        cod_cliente=form.cleaned_data['cod_cliente'],
                        cupo_credito=form.cleaned_data['cupo_credito'],
                    )

                messages.success(request, "Cliente guardado exitosamente")

            except Exception as e:
                messages.error(request, f"Error al cargar la información: {str(e)}")

            return redirect('Clientes')

    return render(request, 'clientes.html', {'form': form})


def editar_Cliente_vista(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
            request.POST, request.FILES, instance=cliente)
        if form.is_valid:
            form.save()
    return redirect('Clientes')
        




def eliminar_Cliente_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                cliente = Cliente.objects.get(pk=id_personal_eliminar)
                persona = cliente.iddocumento
                contacto = persona.idcontacto
                direccion = persona.iddireccion

                cliente.delete()
                persona.delete()
                contacto.delete()
                direccion.delete()

                messages.success(request, "Cliente eliminado exitosamente")
            except Cliente.DoesNotExist:
                messages.error(request, "El cliente no existe")
        else:
            messages.error(request, "No se proporcionó un código de cliente válido")
    else:
        return HttpResponseBadRequest("Solicitud no válida")

    return redirect('Clientes')

#---------------------------- EMPLEADOS ---------------

def empleados_vista(request):
    if not request.user.is_staff:
        return render(request,"home.html")
    empleados = Empleado.objects.all()
    personas = Persona.objects.all()
    cargoempleado = CargoEmpleado.objects.all()
    eps = Eps.objects.all()
    arl = Arl.objects.all()
    fondopension = FondoPension.objects.all()
    usuario = Usuarioid.objects.all()
    rolusuario = RolUsuario.objects.all()
    form_personal = AgregarEmpleadoForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'empleado' : empleados,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
        'cargoempleado' : cargoempleado,
        'eps' : eps,
        'arl' : arl,
        'fondopension' : fondopension,
        'usuario' : usuario,
        'rolsusuario' : rolusuario,
        'personas' : personas,

    }
    return render(request, 'empleados.html', context)

def agregar_Empleado_vista(request):
    if request.method == 'POST':
        form = AgregarEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    ciudad = Ciudad.objects.create(
                        ciudad=form.cleaned_data['ciudad'])


                    contacto = Contacto.objects.create(
                        telefono=form.cleaned_data['telefono'],
                        correo=form.cleaned_data['correo']
                        )
                    
                    direccion = Direccion.objects.create(
                        direccion=form.cleaned_data['direccion'],
                        barrio=form.cleaned_data['barrio'],
                        idciudad=ciudad,
                        )

                    persona = Persona.objects.create(
                        documentoidentidad=form.cleaned_data['documentoidentidad'],
                        primer_nombre=form.cleaned_data['primer_nombre'],
                        segundo_nombre=form.cleaned_data['segundo_nombre'],
                        primer_apellido=form.cleaned_data['primer_apellido'],
                        segundo_apellido=form.cleaned_data['segundo_apellido'],
                        genero=form.cleaned_data['genero'],
                        idcontacto=contacto,
                        iddireccion=direccion
                    )

                    usuario = Usuarioid.objects.create(
                               usuario=form.cleaned_data['usuario'],
                               contrasena=form.cleaned_data['contrasena'])


                    empleado = Empleado.objects.create(
                        iddocumento=persona,
                        idusuario=usuario,
                        idarl=form.cleaned_data['idarl'],
                        ideps=form.cleaned_data['ideps'],
                        idfondo_pension=form.cleaned_data['idfondo_pension'],
                        idrolusuario=form.cleaned_data['idrolusuario'],
                        idcargo_empleado=form.cleaned_data['idcargo_empleado'],
                        cod_empleado=form.cleaned_data['cod_empleado'],
                        fecha_ingreso=form.cleaned_data['fecha_ingreso'],
                        salario=form.cleaned_data['salario'],
                        fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                        rh=form.cleaned_data['rh'],
                    )

                messages.success(request, "Cliente guardado exitosamente")

            except Exception as e:
                messages.error(request, f"Error al cargar la información: {str(e)}")

            return redirect('Empleados')

    return render(request, 'empleados.html', {'form': form})


def editar_Empleado_vista(request):
    cliente = get_object_or_404(Cliente, pk="id_personal_editar")
    if request.method == 'POST':
        form = EditarClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Redireccionar o realizar alguna acción después de guardar los cambios
    else:
        form = EditarClienteForm(instance=cliente)
    return redirect('Empleados')


def eliminar_Empleado_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                empleado = Empleado.objects.get(pk=id_personal_eliminar)
                usuario = empleado.idusuario
                persona = empleado.iddocumento
                contacto = persona.idcontacto
                direccion = persona.iddireccion

                usuario.delete() 
                persona.delete()
                contacto.delete()
                direccion.delete()
                empleado.delete()

                messages.success(request, "Cliente eliminado exitosamente")
            except Cliente.DoesNotExist:
                messages.error(request, "El cliente no existe")
        else:
            messages.error(request, "No se proporcionó un código de cliente válido")
    else:
        return HttpResponseBadRequest("Solicitud no válida")

    return redirect('Empleados')




#------------- PRODUCTOS -------------------

def productos_vista(request):
    
    producto = Producto.objects.all()
    talla = Talla.objects.all()
    categoriaproducto = CategoriaProducto.objects.all()
    form_personal = AgregarProductoForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'producto' : producto,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
        'talla' : talla,
        'categoriaproducto' : categoriaproducto,
    }

    return render(request, 'productos.html', context)

def agregar_Producto_vista(request):
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al guardar el producto")
                return redirect('Productos')

    return redirect('Productos')

"""

def editar_Producto_vista(request):
    cliente = get_object_or_404(Cliente, pk="id_personal_editar")
    if request.method == 'POST':
        form = EditarProductoForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            # Redireccionar o realizar alguna acción después de guardar los cambios
    else:
        form = EditarProdcutoForm(instance=cliente)
    return redirect('Productos')
"""

def eliminar_Producto_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                producto = Producto.objects.get(pk=id_personal_eliminar)

                producto.delete() 

            except Producto.DoesNotExist:
                messages.error(request, "El Producto no existe")

    return redirect('Productos')


#-------------------- Inventario 

def inventarios_vista(request):
    inventario = Inventario.objects.all()
    empleado = Empleado.objects.all()
    producto = Producto.objects.all()
    tipomovimiento = Tipomovimiento
    talla = Talla.objects.all()
    ubicacion = Ubicacioninventario.objects.all()
    form_personal = AgregarInventarioForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'inventario' : inventario,
        'empleado' : empleado,
        'tipomovimiento' : tipomovimiento,
        'producto' : producto,
        'ubicacion' : ubicacion,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
        'talla' : talla,
    }

    return render(request, 'inventarios.html', context)

def agregar_Inventario_vista(request):
    if request.method == 'POST':
        form = AgregarInventarioForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Guardar la entrada de inventario
                inventario = form.save()

                # Obtener el producto correspondiente al código del producto ingresado en el formulario
                codigo_producto = inventario.cod_producto.cod_producto
                producto = Producto.objects.get(cod_producto=codigo_producto)

                # Sumar la cantidad de productos del inventario al total de productos del modelo Producto
                producto.cantidad_productos += inventario.cantidad_productos
                producto.save()

                # Redireccionar a la página de inventarios
                return redirect('Inventarios')

            except Exception as e:
                # Manejar el error si ocurre algún problema
                messages.error(request, f"Error al guardar el Inventario: {str(e)}")
    else:
        form = AgregarInventarioForm()

    return redirect('Inventarios')

def eliminar_Inventario_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                inventario = Inventario.objects.get(pk=id_personal_eliminar)

                inventario.delete() 

            except Inventario.DoesNotExist:
                messages.error(request, "El inventario no existe")

    return redirect('Inventarios')



#-------------------- VENTAS-------------------

def ventas_vista(request):

    venta = Venta.objects.all()
    empleado = Empleado.objects.all()
    producto = Producto.objects.all()
    cliente = Cliente.objects.all()
    form_personal = AgregarVentaForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'venta' : venta,
        'empleado' : empleado,
        'cliente' : cliente,
        'producto' : producto,
        'form_personal' : form_personal,
  #      'form_editar' : form_editar,
    }

    return render(request, 'ventas.html', context)

def agregar_Venta_vista(request):
    if request.method == 'POST':
        form = AgregarVentaForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al guardar el producto")
                return redirect('Ventas')

    return redirect('Ventas')

def eliminar_Venta_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                venta = Venta.objects.get(pk=id_personal_eliminar)

                venta.delete() 

            except Venta.DoesNotExist:
                messages.error(request, "No es posible")

    return redirect('Ventas')

# --------------NOVEDADES PERSONAL -----------------

def novedad_Empleado_vista(request):
    if not request.user.is_staff:
        return render(request,"home.html")
    novedadpersonal = Novedadpersonal.objects.all()
    tiponovedad = Tiponovedadpersonal.objects.all()
    empleado = Empleado.objects.all()
    form_personal = AgregarNovedadEmpleadoForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'novedadpersonal' : novedadpersonal,
        'tiponovedad' : tiponovedad,
  #      'form_editar' : form_editar,
        'empleado' : empleado,
        'form_personal' : form_personal,
    }

    return render(request, 'novedadesempleados.html', context)

def agregar_Novedad_Empleado_vista(request):
    if request.method == 'POST':
        form = AgregarNovedadEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al guardar el producto")
                return redirect('NovedadesEmpleados')

    return redirect('NovedadesEmpleados')

def eliminar_Novedad_Empleado_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                novedadpersonal = Novedadpersonal.objects.get(pk=id_personal_eliminar)

                novedadpersonal.delete() 

            except Novedadpersonal.DoesNotExist:
                messages.error(request, "La Novedad no existe")

    return redirect('NovedadesEmpleados')


# --------------PQRS -----------------

def pqrs_vista(request):
    if not request.user.is_staff:
        return render(request,"home.html")
    pqrs = Pqr.objects.all()
    tipopqrs = TipoPQR.objects.all()
    estadopqrs = EstadoPQR.objects.all()
    empleado = Empleado.objects.all()
    cliente = Cliente.objects.all()
    form_personal = AgregarPqrsForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'pqrs' : pqrs,
        'tipopqrs' : tipopqrs,
  #      'form_editar' : form_editar,
         'empleado' : empleado,
         'estadopqrs': estadopqrs,
         'cliente' : cliente,
        'form_personal' : form_personal,
    }

    return render(request, 'pqrs.html', context)

def agregar_Pqrs_vista(request):
    if request.method == 'POST':
        form = AgregarPqrsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al registrar PQRS")
                return redirect('Pqrs')

    return redirect('Pqrs')

def eliminar_Pqrs_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                pqrs = Pqr.objects.get(pk=id_personal_eliminar)

                pqrs.delete() 

            except Pqr.DoesNotExist:
                messages.error(request, "La PQRS no existe")

    return redirect('Pqrs')


# --------------NOVEDADES PRODUCTOS -----------------

def novedad_Producto_vista(request):
    novedadproducto = Novedadproducto.objects.all()
    tiponovedad = Tiponovedadproducto.objects.all()
    inventario = Inventario.objects.all()
    estadopqrs = EstadoPQR.objects.all()
    empleado = Empleado.objects.all()
    cliente = Cliente.objects.all()
    form_personal = AgregarNovedadProductoForm()
   # form_editar = EditarEmpleadoForm()
    context ={
        'novedadproducto' : novedadproducto,
        'tiponovedad' : tiponovedad,
  #      'form_editar' : form_editar,
         'empleado' : empleado,
         'estadopqrs': estadopqrs,
         'cliente' : cliente,
         'inventario' : inventario,
        'form_personal' : form_personal,
    }

    return render(request, 'novedadesproductos.html', context)

def agregar_Novedad_Producto_vista(request):
    if request.method == 'POST':
        form = AgregarNovedadProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request,"error al registrar Novedad")
                return redirect('novedadesProductos')

    return redirect('novedadesProductos')

def eliminar_Novedad_Producto_vista(request):
    if request.method == 'POST':
        id_personal_eliminar = request.POST.get('id_personal_eliminar')
        if id_personal_eliminar:
            try:
                novedadproducto = Novedadproducto.objects.get(pk=id_personal_eliminar)

                novedadproducto.delete() 

            except Novedadproducto.DoesNotExist:
                messages.error(request, "La PQRS no existe")

    return redirect('novedadesProductos')