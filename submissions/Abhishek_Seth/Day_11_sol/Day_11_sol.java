import java.util.*;
public class Day_11_sol{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int i,arr[]=new int[5];
        System.out.print("Enter numbers: ");
        for ( i = 0; i < 5; i++) {
            arr[i]=sc.nextInt();
        }
        Arrays.sort(arr);
        System.out.print("Sorted List: ");
        for (i = 0; i < 5; i++) {
            System.out.println(arr[i]);
        }
    }
}