# Archivo: sistema_bancario/clientes/cliente.py

class Cliente:
    def __init__(self, num_cuenta, nombre, direccion, saldo): 
        self.num_cuenta = num_cuenta,
        self.nombre = nombre
        self.direccion = direccion
        self.saldo = saldo

    def __str__(self):
        return f"Número de cuenta: {self.num_cuenta}\nCliente: {self.nombre}\nDirección: {self.direccion}\nSaldo: {self.saldo}"
