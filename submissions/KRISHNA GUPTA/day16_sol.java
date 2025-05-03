import java.util.*;
public class day16_sol {
    public static void main(String[] args) {
        System.out.print("Enter a number: ");
        Scanner sc= new Scanner (System.in);
        int n, i, fact=1;
        n=sc.nextInt();
        for(i=1; i<=n; i++)
        {
            fact*=i;
        }
        System.out.println("Factorial of "+ n + " is " + fact);
        
    }
    
}
