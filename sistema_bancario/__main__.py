# Archivo: sistema_bancario/__main__.py
from sistema_bancario.clientes.cliente import Cliente
from sistema_bancario.empleados.empleado import Empleado
from sistema_bancario.transacciones.transaccion import Transaccion

db_socios =[
    {
    "num_cuenta": "0000000001",
    "nombre": "Alice",
    "direccion": "123 Main St",
    "saldo": 1000,
    },
    {
    "num_cuenta": "0000000002",
    "nombre": "Bob",
    "direccion": "456 Elm St",
    "saldo": 2000,
    },
    {
    "num_cuenta": "0000000003",
    "nombre": "Eva",
    "direccion": "345",
    "saldo": 5000,
    },
    {
    "num_cuenta": "0000000004",
    "nombre": "Alex",
    "direccion": "978",
    "saldo": 3000,
    },
]

def verificar_usuario(num_cuenta):
    for usuario in db_socios:
        if usuario["num_cuenta"] == num_cuenta:
            return True
    return False

def obtener_saldo(num_cuenta):
    for usuario in db_socios:
        if usuario["num_cuenta"] == num_cuenta:
            return usuario["saldo"]
    return None


def main():
    num_cuenta_usuario = input("Ingrese su número de cuenta: ")
    num_cuenta_beneficiario = input("Ingrese el número de cuenta del beneficiario: ")
    monto = float(input("Ingrese el monto de la transacción: "))
    
    if verificar_usuario(num_cuenta_beneficiario):
        saldo = obtener_saldo(num_cuenta_usuario)
        print(f"El saldo de la cuenta {num_cuenta_usuario} es: {saldo}")
        if saldo > monto:
            transaccion1 = Transaccion(num_cuenta_usuario, num_cuenta_beneficiario, monto)
            print("Transaccion realizada:")
            print(transaccion1)
            print(f"El saldo de la cuenta {num_cuenta_usuario} es: {saldo-monto}")
        else:
            print(f"No cuenta con saldo suficiente para realizar la transaccion, {num_cuenta_usuario} su saldo es: {saldo}")
        
    else:
        print(f"Usuario con numero de cuenta {num_cuenta_beneficiario} no se ha encontrado en la base de datos.")

if __name__ == "__main__":
    main()
