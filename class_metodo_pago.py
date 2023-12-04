from CLIENTES.class_cliente import Clientes

class Metodo_pago (Clientes):
    def __init__(self, nombre, apellido, num_cliente, direccion, telefono, met_pago, tarjeta, mp, efec):
        super().__init__(nombre, apellido, num_cliente, direccion, telefono)
        self.met_pago = True
        self.tarjeta = tarjeta
        self.mp = mp
        self.efec = efec




    def compra(self):
       input("ingrese el metodo de pago")
       if Metodo_pago == self.efec:
          return f"el cliente ha seleccionado pagar con {self.efec}"
       if Metodo_pago == self.mp:
          return f"el cliente ha seleccionado pagar con {self.mp}"
       elif Metodo_pago == self.tarjeta:
          return f"el cliente ha seleccionado pagar con {self.tarjeta}"
       else:
          return f"seleccione un metodo de pago valido"