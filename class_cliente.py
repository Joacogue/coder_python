class Clientes:

    def __init__(self, nombre, apellido, num_cliente, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.num_cliente = num_cliente
        self.direccion = direccion
        self.telefono = telefono

    def getnombre(self):
        return self.nombre

    def getapellido(self):
        return self.apellido

    def incio_sesion(self):
        return f"Hola {self.nombre}, inicio de sesion exitoso"

    def compra(self):
        return "su compra se ha realizado con exito"
    def mostrarCliente(self):
        return ("\nNombres: " +self.getnombre()+"\nApellido: "+self.getapellido() )

    def __str__(self):
        return "%s , %s" % (self.nombre, self.apellido)

nombres = input("por favor ingrese su(s) nombre(s)" )
apellido = input("por favor ingrese su(s) apellido(s)" )

e = Clientes()
e.mostrarCliente()
