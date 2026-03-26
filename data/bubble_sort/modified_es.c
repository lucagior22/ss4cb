#include <stdio.h>

void ordenamiento_burbuja(int arreglo_numerico[], int longitud_arreglo)
{
    /* Ordena el arreglo_numerico en orden ascendente usando ordenamiento burbuja */
    int pasaje_externo;
    int pasaje_interno;
    int valor_temporal;
    int intercambiado;

    for (pasaje_externo = 0; pasaje_externo < longitud_arreglo - 1; pasaje_externo++)
    {
        intercambiado = 0;
        for (pasaje_interno = 0; pasaje_interno < longitud_arreglo - pasaje_externo - 1; pasaje_interno++)
        {
            if (arreglo_numerico[pasaje_interno] > arreglo_numerico[pasaje_interno + 1])
            {
                /* intercambio de elementos adyacentes*/
                valor_temporal = arreglo_numerico[pasaje_interno];
                arreglo_numerico[pasaje_interno] = arreglo_numerico[pasaje_interno + 1];
                arreglo_numerico[pasaje_interno + 1] = valor_temporal;
                intercambiado = 1;
            }
        }
        /* Si no ocurre un intercambio en este pasaje, el arreglo ya esta ordenado */
        if (intercambiado == 0)
            break;
    }
}