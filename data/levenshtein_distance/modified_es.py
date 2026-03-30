def distancia_levenshtein(origen: str, fin: str) -> int:
    """
    Computa la distancia Levenshtein entre dos cadenas.

    La distancia Levenshtein esta definifa como el mínimo número de
    ediciones de un caracter (inserciones, borradas o sustituciones)
    requeridas para cambiar un string en otro.

    Esta implementación usa programación dinámica para construir una matriz
    de las distancias entre todos los prefijos de dos cadenas.

    Argumentos:
        origen (str): La cadena fuente.
        end (str): La cadena objetivo.

    Retorna
        int: La distancia de Levenshtein entre dos cadenas
    """

    # Obtener las longitudes de ambos strings
    long_origen = len(origen)
    long_fin = len(fin)

    # Crear una matriz (long_origen + 1) x (long_fin + 1)
    # dp[i][j] contendrá la distancia entre
    # origen[:i] y fin[:j]
    dp = [[0 for _ in range(long_fin + 1)] for _ in range(long_origen + 1)]


    # Inicializar la primera columna (transformar origen -> cadena vacía)
    for i in range(long_origen + 1):
        dp[i][0] = i  # i borradas

    # Inicializar la primera fila (transforma la cadena vacia -> fin)
    for j in range(long_fin + 1):
        dp[0][j] = j  # j inserciones

    # Llenar la matriz
    for i in range(1, long_origen + 1):
        for j in range(1, long_fin + 1):
            # Si los caracteres coinciden, ninguna operación es necesaria
            if origen[i - 1] == fin[j - 1]:
                coste = 0
            else:
                coste = 1

            # Computar el mínimo de
            # - Borrado
            # - Inserción
            # - Sustitución
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # borrado
                dp[i][j - 1] + 1,      # inserción
                dp[i - 1][j - 1] + coste  # substitución
            )
    # La celda inferior derecha contiene la respuesta
    return dp[long_origen][long_fin]
