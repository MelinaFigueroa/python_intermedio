# cuenta_bancaria.py
from abc import ABC, abstractmethod
from datetime import date

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular: str, dni_titular: int, fecha_nacimiento: date, saldo: float = 0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self._saldo = saldo

    @abstractmethod
    def depositar(self, monto: float):
        """Deposita un monto positivo en la cuenta."""
        pass

    @abstractmethod
    def extraer(self, monto: float):
        """Extrae un monto si hay fondos suficientes."""
        pass

    def obtener_saldo(self) -> float:
        return self._saldo

    def _calcular_edad(self) -> int:
        hoy = date.today()
        años = hoy.year - self._fecha_nacimiento.year
        # Ajuste si no cumplió años este año
        if (hoy.month, hoy.day) < (self._fecha_nacimiento.month, self._fecha_nacimiento.day):
            años -= 1
        return años

    def obtener_edad(self) -> int:
        return self._calcular_edad()
