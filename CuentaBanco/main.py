# main.py
from datetime import date
from cuenta_corriente import CuentaCorriente
from cuenta_ahorro    import CuentaAhorro

# ——— Pruebas Cuenta Corriente ———
cc = CuentaCorriente("Melina", 33985365, date(1989, 10, 2), saldo=1000)
print("=== Cuenta Corriente ===")
print("Saldo inicial:", cc.obtener_saldo())

# 1. Depósito válido
print("\n1) Depositar 200")
cc.depositar(200)
print("Saldo:", cc.obtener_saldo())

# 2. Depósito negativo
print("\n2) Depositar -50 (esperamos ValueError)")
try:
    cc.depositar(-50)
except ValueError as e:
    print("Error:", e)
print("Saldo tras intento:", cc.obtener_saldo())

# 3. Extracción válida
print("\n3) Extraer 300")
try:
    cc.extraer(300)
except ValueError as e:
    print("Error:", e)
print("Saldo:", cc.obtener_saldo())

# 4. Extracción por encima del límite
print("\n4) Extraer 10000 (sobre límite)")
try:
    cc.extraer(10000)
except ValueError as e:
    print("Error:", e)
print("Saldo:", cc.obtener_saldo())

# 5. Extracción con saldo insuficiente
print("\n5) Extraer 2000 (saldo insuficiente)")
try:
    cc.extraer(2000)
except ValueError as e:
    print("Error:", e)
print("Saldo:", cc.obtener_saldo())

# ——— Pruebas Cuenta Ahorro ———
ca = CuentaAhorro("María", 44444444, date(1985, 7, 15), saldo=500)
print("\n=== Cuenta Ahorro ===")
print("Saldo inicial:", ca.obtener_saldo())

# 6. Depósito válido
print("\n6) Depositar 100")
ca.depositar(100)
print("Saldo:", ca.obtener_saldo())

# 7. Depósito cero
print("\n7) Depositar 0 (esperamos ValueError)")
try:
    ca.depositar(0)
except ValueError as e:
    print("Error:", e)
print("Saldo:", ca.obtener_saldo())

# 8. Aplicar interés
print("\n8) Aplicar interés")
ca.aplicar_interes()
print("Saldo después de interés:", ca.obtener_saldo())

# 9. Extracción válida
print("\n9) Extraer 50")
try:
    ca.extraer(50)
except ValueError as e:
    print("Error:", e)
print("Saldo:", ca.obtener_saldo())

# 10. Extracción negativa
print("\n10) Extraer -30 (esperamos ValueError)")
try:
    ca.extraer(-30)
except ValueError as e:
    print("Error:", e)
print("Saldo:", ca.obtener_saldo())

# 11. Extracción con saldo insuficiente
print("\n11) Extraer 1000 (saldo insuficiente)")
try:
    ca.extraer(1000)
except ValueError as e:
    print("Error:", e)
print("Saldo:", ca.obtener_saldo())
