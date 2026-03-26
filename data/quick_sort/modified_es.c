#include <stdio.h>

void intercambiar_elementos(int *primer_elemento, int *segundo_elemento)
{
    int valor_temporal = *primer_elemento;
    *primer_elemento = *segundo_elemento;
    *segundo_elemento = valor_temporal;
}

int particionar_arreglo(int numero_arreglo[], int indice_inferior, int indice_superior)
{
    int valor_pivote = numero_arreglo[indice_superior];
    int indice_elemento_menor = indice_inferior - 1;
    int indice_actual;

    for (indice_actual = indice_inferior; indice_actual < indice_superior; indice_actual++)
    {
        if (numero_arreglo[indice_actual] <= valor_pivote)
        {
            indice_elemento_menor++;
            intercambiar_elementos(&numero_arreglo[indice_elemento_menor], &numero_arreglo[indice_actual]);
        }
    }
    intercambiar_elementos(&numero_arreglo[indice_elemento_menor + 1], &numero_arreglo[indice_superior]);
    return indice_elemento_menor + 1;
}

void ordenamiento_rapido(int numero_arreglo[], int indice_inferior, int indice_superior)
{
    if (indice_inferior < indice_superior)
    {
        int indice_pivote = particionar_arreglo(numero_arreglo, indice_inferior, indice_superior);
        ordenamiento_rapido(numero_arreglo, indice_inferior, indice_pivote - 1);
        ordenamiento_rapido(numero_arreglo, indice_pivote + 1, indice_superior);
    }
}
