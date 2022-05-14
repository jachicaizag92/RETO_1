""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Oscar Franco-Bedoya
    Mayo 3-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)-------------
def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un número para realizar la operación.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular división: (4)")
  print("==================================================")
   
  opcion = input("ingrese la opcion: ")
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
operacion=menu_operaciones()

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

if operacion == '1':
  print("Por favor ingrese los numeros a sumar")
  numero_uno = float(input("ingrese el numero_uno: "))
  numero_dos = float(input("ingrese el numero_dos: "))
  print(f"El resultado de la operacion es: {calc.sumar_numeros(numero_uno,numero_dos)}")
elif operacion == '2':
  print("Por favor ingrese los numeros a restar")
  numero_uno = float(input("ingrese el numero_uno: "))
  numero_dos = float(input("ingrese el numero_dos: "))
  print(f"El resultado de la operacion es: {calc.restar_numeros(numero_uno,numero_dos)}")
elif operacion == '3':
  print("Por favor ingrese los numeros a multiplicar")
  numero_uno = float(input("ingrese el numero_uno: "))
  numero_dos = float(input("ingrese el numero_dos: "))
  print(f"El resultado de la operacion es: {calc.multiplicar_numeros(numero_uno,numero_dos)}")
elif operacion == '4':
  print("Por favor ingrese los numeros a dividir")
  numero_uno = float(input("ingrese el numero_uno: "))
  numero_dos = float(input("ingrese el numero_dos: "))
  print(f"El resultado de la operacion es: {calc.dividir_numeros(numero_uno,numero_dos)}") 
else:
  print("Parametros invalidos")
  
