print ("\nSituacion C2")
print ("")

valor1 = int(input("Ingrese el primer valor:"))
valor2 = int(input("Ingrese el segundo valor:"))
valor3 = int(input("ingrese el tercer valor:"))

promedio = (valor1 + valor2 + valor3) / 3
print ("\nEl promedio es:",promedio)

if valor1 >= promedio:
	print ("\nEl primer valor ingresado es mayor/igual al promedio")
else:
	print ("\nEl primer valor no es mayor/igual al promedio")
if valor2 >= promedio:
	print ("\nEl segundo valor ingresado es mayor/igual al promedio")
else:
	print ("\nEl segundo valor no es mayor/igual al promedio")
if valor3 >= promedio:
	print ("\nEl tercer valor ingresado es mayor/igual al promedio")
else:
	print ("\nEl tercer valor no es mayor/igual al promedio")



