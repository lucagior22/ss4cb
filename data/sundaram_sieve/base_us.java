import java.util.*;

public class base_us {

    public static List<Integer> sieve(int n) {
        int limit = (n - 1) / 2;
        boolean[] marked = new boolean[limit + 1];

        // Step 1: mark numbers of the form i + j + 2ij
        for (int i = 1; i <= limit; i++) {
            for (int j = i; (i + j + 2 * i * j) <= limit; j++) {
                marked[i + j + 2 * i * j] = true;
            }
        }

        // Step 2: collect primes
        List<Integer> primes = new ArrayList<>();

        if (n > 2) {
            primes.add(2); // only even prime
        }

        for (int i = 1; i <= limit; i++) {
            if (!marked[i]) {
                primes.add(2 * i + 1);
            }
        }

        return primes;
    }
}