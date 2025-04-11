# Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
    
# Escribe un programa que intente sumar un número y una cadena. Si se produce un error
# de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
try:
    numero = 10
    cadena = "hola"
    resultado = numero + cadena
    print(resultado)
except TypeError:
    print("Error: No se puede sumar un número con una cadena.")

# Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
# Si se produce una excepción KeyError, captura la excepción y muestra mensaje de error al usuario.
try:
    mi_diccionario = {"nombre": "Juan", "edad": 30}
    valor = mi_diccionario["apellido"]
    print(valor)
except KeyError:
    print("Error: La clave no existe en el diccionario.")

# Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
# FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
# embargo, también intenta crear el archivo si no existe.
nombre_archivo = "archivo_prueba.txt"

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo {nombre_archivo} no existe. Creándolo ahora...")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Este es un nuevo archivo creado automáticamente.")
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Escribe un programa que intente dividir dos números. Si el segundo número es cero,
# captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
# captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Ingrese un número válido.")