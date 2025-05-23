# cuenta_corriente.py
from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, limite_extraccion=500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self._saldo += monto
        print(f"Se depositaron {monto:.2f}. Saldo actual: {self._saldo:.2f}")

    def extraer(self, monto: float):
        if monto > self._limite_extraccion:
            raise ValueError(f"No puede extraer más de {self._limite_extraccion:.2f} en una sola operación.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= monto
        print(f"Se extrajeron {monto:.2f}. Saldo actual: {self._saldo:.2f}")
