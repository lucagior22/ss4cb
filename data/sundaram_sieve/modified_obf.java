import java.util.*;

public class modified_obf {
    public static List<Integer> f(int n) {
        int l = (n - 1) / 2;
        boolean[] m = new boolean[l + 1];

        for (int i = 1; i <= l; i++) {
            for (int j = i; (i + j + 2 * i * j) <= l; j++) {
                m[i + j + 2 * i * j] = true;
            }
        }

        List<Integer> p = new ArrayList<>();

        if (n > 2) {
            p.add(2);
        }

        for (int i = 1; i <= l; i++) {
            if (!m[i]) {
                p.add(2 * i + 1);
            }
        }

        return p;
    }
}
