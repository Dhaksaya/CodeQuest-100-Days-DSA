import java.util.*;
public class Day15_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numbers: ");
        String a = sc.nextLine();
        String[] arr= a.trim().split("\\s+");
        int s = 0;
        for (String i: arr) {
            s += Integer.parseInt(i);
            }
        System.out.println("Secret Code: " + s);
    }
}