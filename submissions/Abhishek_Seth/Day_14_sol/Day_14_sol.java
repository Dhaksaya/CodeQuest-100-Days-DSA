import java.util.*;
public class Day_14_sol{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string: ");
        String a= sc.nextLine();
        int l=a.length();
        char b;
        String c="";
        for (int i = 0; i < l; i++) {
            b=a.charAt(i);
            if(b=='_'){
                c=c+ (char)(a.charAt(i-1)+1);
            }
            else{
                c=c+b;
            }
        }
        System.out.println("Restored string: "+c);
    }
}