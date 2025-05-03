import java.util.*;
public class Day17_sol {
    public static void main(String[] args) {
        Scanner sc= new Scanner (System.in);
        int i, n;
        int a=0, b=1;
        int nxtTerm=a+b;
        System.out.print("Enter the number of terms: ");
        n=sc.nextInt();

        if (n==1)
        {
            System.out.print("Fibonacci sequence: "+ a);

        }
        else 
        {
            System.out.print("Fibonacci sequence: "+a+" "+b+" ");
        for (i=3; i<=n; ++i)
        {
            System.out.print(nxtTerm + " ");
            a=b;
            b=nxtTerm;
            nxtTerm=a+b;
        }

        }
        
        

        
    }
    
}
