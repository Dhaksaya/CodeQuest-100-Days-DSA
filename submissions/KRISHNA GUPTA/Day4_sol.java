import java.util.*;
public class Day4_sol{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n;
        System.out.print("Enter a number:");
        n=sc.nextInt();
        int last_dgt, dgt_sum=0;
        StringBuilder breakdown = new StringBuilder();
        while(n>0)
        {
            last_dgt=n%10;
            breakdown.insert(0, last_dgt + (breakdown.length() > 0 ? " + " : ""));
            n=n/10;
            dgt_sum+=last_dgt;
        }
        System.out.println("Sum of digits:"+ breakdown + " = " + dgt_sum);
    }
}