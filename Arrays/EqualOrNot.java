//Check if two arrays are equal or not
import java.util.Arrays;
import java.util.Scanner;
public class EqualOrNot {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the size of the arrays: ");
        int size = sc.nextInt();
        int[] arr1 = new int[size];
        int[] arr2 = new int[size];
        System.out.println("Enter elements of the first array:");
        for (int i = 0; i < size; i++) {
            arr1[i] = sc.nextInt();
        }
        System.out.println("Enter elements of the second array:");
        for (int i = 0; i < size; i++) {
            arr2[i] = sc.nextInt();
        }

        if (Arrays.equals(arr1, arr2)) {
            System.out.println("The arrays are equal.");
        } else {
            System.out.println("The arrays are not equal.");
        }
    }
}
