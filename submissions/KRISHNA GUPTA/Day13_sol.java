import java.util.*;
public class Day13_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        boolean hasEven = false;
        System.out.print("Enter N: ");
        n=sc.nextInt();
        sc.close();

        String str = String.valueOf(n);
        System.out.print("Even Digits: ");
        for (int i=0; i<str.length(); i++)
        {
            char ch = str.charAt(i);
            if (Character.isDigit(ch) && (ch - '0') % 2 == 0) {
                System.out.print(ch+" ");
                hasEven = true;
            }
        }

        if (!hasEven) {
            System.out.println("No even digits found!");
            
        } 
    }
    
}
