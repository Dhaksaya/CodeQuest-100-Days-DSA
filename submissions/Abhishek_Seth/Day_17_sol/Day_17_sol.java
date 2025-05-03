import java.util.*;
public class Day_17_sol{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int n = sc.nextInt();
        System.out.print("Fibonacci sequence: ");
        Day_17_sol obj = new Day_17_sol();
        obj.fibo(0,1,n);
    }
    void fibo(int a,int b,int n){
        if(n>0){
            System.out.print(a+" ");
            fibo(b,(a+b),n-1);
        }
    }
}