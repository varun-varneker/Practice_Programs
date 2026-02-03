// You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner n=new Scanner(System.in);
        int a=n.nextInt();
        int[] arr=new int[a];
        for(int i=0;i<a;i++){
            arr[i]=n.nextInt();
        }
        int L = a+1;
        int original = L*(L+1)/2;
        int sum = 0;
        for (int i = 0;i<a; i++){
          sum = sum+arr[i];
        }
        System.out.print(original-sum);
        }
      
    
}