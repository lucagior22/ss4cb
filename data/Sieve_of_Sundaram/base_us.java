import java.util.*;

public class base_us {

    public static List<Integer> sieve(int upperLimit) {
        int limit = (upperLimit - 1) / 2;
        boolean[] marked = new boolean[limit + 1];

        
        for (int i = 1; i <= limit; i++) {
            for (int j = i; (i + j + 2 * i * j) <= limit; j++) {
                marked[i + j + 2 * i * j] = true;
            }
        }

        List<Integer> primes = new ArrayList<>();

        if (upperLimit > 2) {
            primes.add(2);

            for (int i = 1; i <= limit; i++) {
                if (!marked[i]) {
                    primes.add(2 * i + 1);
                }
            }
        }

        return primes;
    }

}
