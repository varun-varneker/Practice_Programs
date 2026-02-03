import java.util.*;
class SearchElement {
    public static void main(String[] args) {
    Scanner z = new Scanner(System.in);
    int n = z.nextInt();
    int[] arr = new int[n];
    for(int i = 0; i<n; i++){
        arr[i]=z.nextInt();
    }
    int target = z.nextInt();
    for(int i = 0; i<n;i++){
        if(arr[i]==target){
            System.out.print("Target element present in "+i);
        }
    }
    }
}