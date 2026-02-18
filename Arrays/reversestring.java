import java.util.Arrays;
public class reversestring {
int[] arr = {1,2,3,4,5};
int n = arr.length;

int first = arr[0];  // store first element

    for(int i = 0; i < n-1; i++) {
      arr[i] = arr[i+1];  // shift left
}

arr[n-1] = first;  // put first at end
}