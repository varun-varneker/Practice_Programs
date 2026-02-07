// Find the repeating number in an array of n+1 integers where each integer is between 1 and n (inclusive).
import java.util.HashSet;

public class FindDuplicate {
    public static void main(String[] args) {
        int[] arr = {1, 3, 4, 2, 3};

        HashSet<Integer> set = new HashSet<>();

        for (int num : arr) {
            if (!set.add(num)) {
                System.out.println("Repeating number: " + num);
                break;
            }
        }
    }
}
