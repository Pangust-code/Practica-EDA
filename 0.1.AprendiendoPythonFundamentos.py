"""Resumen practico de fundamentos Python usados en la guia 0.1.

Este archivo no reemplaza la guia original, pero deja ejemplos minimos
alineados con las bases necesarias para la practica EDA.
"""


def ejemplos_basicos() -> None:
    # Variables y tipos
    mensaje = "Hola Python"
    numero = 10
    decimal = 3.14
    bandera = True

    print(mensaje, type(mensaje))
    print(numero, type(numero))
    print(decimal, type(decimal))
    print(bandera, type(bandera))

    # Listas y diccionarios
    lista = [3, 1, 2]
    lista.sort()
    print("Lista ordenada:", lista)

    dic = {"edad": 45, "colesterol": 230}
    print("Diccionario:", dic)

    # Funcion
    def clasificar_riesgo(colesterol: int) -> str:
        if colesterol >= 240:
            return "alto"
        if colesterol >= 200:
            return "limite"
        return "normal"

    print("Riesgo segun colesterol 230:", clasificar_riesgo(230))


if __name__ == "__main__":
    ejemplos_basicos()
