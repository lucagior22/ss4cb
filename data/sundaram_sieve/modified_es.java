import java.util.*;

public class modified_es {

    public static List<Integer> sieve(int limiteSuperior) {
        int limite = (limiteSuperior - 1) / 2;
        boolean[] marcado = new boolean[limite + 1];

        // Paso 1: Marcar los numerros de la forma i + j + 2ij
        for (int i = 1; i <= limite; i++) {
            for (int j = i; (i + j + 2 * i * j) <= limite; j++) {
                marcado[i + j + 2 * i * j] = true;
            }
        }

        // Paso 2: recolectar los primos
        List<Integer> primos = new ArrayList<>();

        if (limiteSuperior > 2) {
            primos.add(2); // solo el primo
        }

        for (int i = 1; i <= limite; i++) {
            if (!marcado[i]) {
                primos.add(2 * i + 1);
            }
        }

        return primos;
    }

}
