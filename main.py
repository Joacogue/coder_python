from CLIENTES.class_cliente import *
from CLIENTES.class_metodo_pago import Metodo_pago


Matias = Clientes(nombre = "Matias", apellido = "Gomez", num_cliente = 302, direccion = "av. Diaz Velez 2845", telefono = 1154862540,)
Matias = Metodo_pago(met_pago = True)
print(Matias.mostrarCliente())
print(Matias.incio_sesion())
print(Matias.compra())


