import sys

# --- Funciones auxiliares ---
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

# --- Ejercicio 1 ---
def mayor_de_dos_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        mayor = num1 if num1 > num2 else num2
        print(f"El número mayor es: {mayor}")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

# --- Ejercicio 2 ---
def buscar_palabra_args(args):
    if len(args) < 2:
        print("Error: Debe proporcionar una palabra a buscar y al menos una palabra en la lista.")
        return

    palabra, *lista = args
    resultado = f"La palabra '{palabra}' está en la lista" if palabra in lista else f"La palabra '{palabra}' no está en la lista"
    print(resultado)

def buscar_palabra_interactivo():
    palabra = input("Ingrese la palabra a buscar: ")
    lista = input("Ingrese una lista de palabras separadas por espacios: ").split()
    resultado = f"La palabra '{palabra}' está en la lista" if palabra in lista else f"La palabra '{palabra}' no está en la lista"
    print(resultado)

# --- Ejercicio 3 ---
def par_o_impar():
    try:
        numero = int(input("Ingrese un número: "))
        resultado = "par" if numero % 2 == 0 else "impar"
        print(f"El número {numero} es {resultado}.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")

# --- Ejercicio 4 ---
def calcular_promedio_args(args):
    entrada = input("Ingrese exactamente 3 números separados por espacios: ").split()

    if len(entrada) != 3:
        print("Error: Debe ingresar exactamente 3 valores.")
        return

    # Verificamos que todos sean números
    for i, val in enumerate(entrada):
        if not es_numero(val):
            print(f"Error: El valor '{val}' en la posición {i+1} no es un número. Solo se permiten números.")
            return

    # Convertimos y calculamos
    numeros = [float(n) for n in entrada]
    promedio = sum(numeros) / 3
    print(f"El promedio de {numeros} es: {promedio}")

# --- Menú interactivo ---
def menu():
    while True:
        print("\n=== MENÚ DE EJERCICIOS ===")
        print("1. Calcular el mayor de dos números")
        print("2. Buscar una palabra en una lista")
        print("3. Determinar si un número es par o impar")
        print("4. Calcular promedio de números")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mayor_de_dos_numeros()
        elif opcion == "2":
            buscar_palabra_interactivo()
        elif opcion == "3":
            par_o_impar()
        elif opcion == "4":
            calcular_promedio_args()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        argumentos = sys.argv[2:]
        if comando == "2":
            buscar_palabra_args(argumentos)
        elif comando == "4":
            calcular_promedio_args(argumentos)
        else:
            menu()
    else:
        menu()
