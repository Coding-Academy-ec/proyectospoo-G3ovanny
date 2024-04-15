# Archivo: sistema_bancario/empleados/empleado.py

class Empleado:
    def __init__(self, num_cuenta, nombre, cargo, salario):
        self.num_cuenta = num_cuenta,
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Número de cuenta: {self.num_cuenta}\nEmpleado: {self.nombre}\nCargo: {self.cargo}\nSalario: {self.salario}"
