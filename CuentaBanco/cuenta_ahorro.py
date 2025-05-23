# cuenta_ahorro.py
from cuenta_bancaria import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0, tasa_interes: float = 0.001):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._tasa_interes = tasa_interes  # atributo privado

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self._saldo += monto
        print(f"Se depositaron {monto:.2f}. Saldo actual: {self._saldo:.2f}")

    def extraer(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser positivo.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= monto
        print(f"Se extrajeron {monto:.2f}. Saldo actual: {self._saldo:.2f}")

    def calcular_interes(self) -> float:
        """Calcula el interés generado sobre el saldo actual."""
        return self._saldo * self._tasa_interes

    def aplicar_interes(self):
        """Aplica el interés al saldo."""
        interes = self.calcular_interes()
        self._saldo += interes
        print(f"Se aplicó interés de {interes:.2f}. Nuevo saldo: {self._saldo:.2f}")
