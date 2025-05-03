import java.util.*;
public class Day20_sol
{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int n;
        System.out.print("Enter a number: ");
        n=sc.nextInt();
        Boolean isPrime= true;
        for(int i=2; n>=(i*i); i++)
        {
            if (n%i==0)
            {
                isPrime=false;
                break;
            }
        }
        if (isPrime==true)
        {
            System.out.print("Prime");
        }
        else
        {
            System.out.println("Not prime");
        }
        
        
    }
}
