import java.util.*;
public class Day_9_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the secret message: ");
        String a= sc.nextLine();
        String c="";
        for (int i =a.length()-1; i >=0; i--) {
            c=c+a.charAt(i);
        }
        System.out.println(c);
    }
}