def busqueda_lineal(lista_de_elementos, valor_objetivo):
    """
    Busco por valor_objetivo en la lista de elementos evaluando cada elemento secuencialmente
    Retorna el indice del valor_objetivo si lo encontro o -1 si no esta presente.
    """
    indice_actual = 0
    while indice_actual < len(lista_de_elementos):
        elemento_actual = lista_de_elementos[indice_actual]
        if elemento_actual == valor_objetivo:
            return indice_actual
        indice_actual += 1
    return -1