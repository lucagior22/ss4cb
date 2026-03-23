def busqueda_binaria(numeros_ordenados: list[int], valor_buscado: int) -> int:
    """
    Realiza la busqueda binaria sobre una lista ordenada.

    Args:
        numeros_ordenados (list[int]): Una lista de enteros ordenada en orden ascendente.
        valor_buscado (int): El valor que se esta buscando.

    Returns:
        int: El índice del valor buscado si se encuentra, de otra manera -1.
    """

    # Inicializa los limites del espacio de busqueda
    indice_izquierdo = 0
    indice_derecho = len(numeros_ordenados) - 1

    # Continua buscando mientras el espacio de busqueda sea valido
    while indice_izquierdo <= indice_derecho:

        # Busca el indice medio del espacio de busqueda actual
        indice_medio = (indice_izquierdo + indice_derecho) // 2
        middle_value = numeros_ordenados[indice_medio]

        # Caso 1: Valor encontrado
        if middle_value == valor_buscado:
            return indice_medio

        # Caso 2: Valor es menor →  busco en la mitad de la izquierda
        elif valor_buscado < middle_value:
            indice_derecho = indice_medio - 1

        # Caso 3: Valor es mayor → busco en la mitad de la derecha
        else:
            indice_izquierdo = indice_medio + 1

    # Valor no encontrado
    return -1