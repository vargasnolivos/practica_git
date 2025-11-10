"""
Nombre: Ivan Josue Quimi Ramirez
Paralelo: B
Fecha: 16-05-2025
"""

# Metodos
class ListaOperaciones:
    def __init__(self):
        self._lista = []

    # Ingresar elementos en una lista, definiendo un límite
    def ingresar_valores(self, limite):
        contador = 0
        for i in range(limite):
            print(f"Ingrese el valor {i+1}:")
            opcion = int(input("> "))
            self._lista.append(opcion)
            contador += 1
        print(f"Total de elementos ingresados a la lista: {len(self._lista)}")

    # Eliminar elementos de la lista
    def eliminar_valores(self):
        if not self._lista:
            print("Lista vacía. Regrese e ingrese elementos a la lista...")
        else:
            numero = int(input("Ingrese el valor que desea eliminar: "))
            if numero in self._lista:
                self._lista.remove(numero)
                print(f"Se eliminó el valor {numero}.")
            else:
                print("El valor que ingresó no está en la lista.")

    # Mostrar todos los elementos y resultados
    def mostrar_lista(self):
        print("============================================")
        if not self._lista:
            print("La lista está vacía.")
        else:
            print(f"Elementos en la lista: {self._lista}")
            print(f"Promedio: {self.promedio(mostrar=False)}")
            print(f"Número mayor: {self.numero_mayor(mostrar=False)}")
            print(f"Lista ordenada: {self.ordenar_lista(mostrar=False)}")
        print("============================================")

    # Calcular promedio
    def promedio(self, mostrar=True):
        if not self._lista:
            if mostrar: print("La lista está vacía. No se puede calcular el promedio.")
            return None
        promedio = sum(self._lista) / len(self._lista)
        if mostrar:
            print(f"El promedio de los valores es: {promedio}")
        return promedio

    # Calcular factorial de un número y mostrar lista de pasos
    def factorial(self):
        numero = int(input("Ingrese un número para calcular el factorial: "))
        if numero < 0:
            print("No se puede calcular el factorial de un número negativo.")
            return
        lista_fact = [i for i in range(1, numero + 1)]
        factorial = 1
        for n in lista_fact:
            factorial *= n
        print(f"Valores utilizados en el factorial: {lista_fact}")
        print(f"El factorial de {numero} es: {factorial}")

    # Calcular serie de Fibonacci y almacenarla en lista
    def fibonacci(self):
        n = int(input("Ingrese la cantidad de términos de la serie Fibonacci: "))
        lista_fibo = []
        a, b = 0, 1
        for _ in range(n):
            lista_fibo.append(a)
            a, b = b, a + b
        print(f"Serie de Fibonacci con {n} términos: {lista_fibo}")

    # Encontrar el número mayor
    def numero_mayor(self, mostrar=True):
        if not self._lista:
            if mostrar: print("La lista está vacía. No se puede encontrar el número mayor.")
            return None
        mayor = max(self._lista)
        if mostrar:
            print(f"El número mayor en la lista es: {mayor}")
        return mayor

    # Ordenar la lista
    def ordenar_lista(self, mostrar=True):
        if not self._lista:
            if mostrar: print("La lista está vacía. No se puede ordenar.")
            return []
        lista_ordenada = sorted(self._lista)
        if mostrar:
            print(f"Lista ordenada: {lista_ordenada}")
        return lista_ordenada

    # Menú principal
    def menu(self):
        while True:
            print("\n========== MENU PRINCIPAL ==========")
            print("1. Ingresar elementos a la lista")
            print("2. Eliminar elementos de una lista")
            print("3. Mostrar elementos y resultados")
            print("4. Calcular factorial de un número")
            print("5. Calcular serie de Fibonacci")
            print("6. Salir")
            print("====================================")
            opcion = int(input("> "))

            if opcion == 1:
                print("Ingrese la cantidad de elementos que desea ingresar:")
                cantidad = int(input("> "))
                self.ingresar_valores(cantidad)
            elif opcion == 2:
                self.eliminar_valores()
            elif opcion == 3:
                self.mostrar_lista()
            elif opcion == 4:
                self.factorial()
            elif opcion == 5:
                self.fibonacci()
            elif opcion == 6:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Ingrese un número del menú.")

# Ejecución principal
if __name__ == "__main__":
    c = ListaOperaciones()
    c.menu()
