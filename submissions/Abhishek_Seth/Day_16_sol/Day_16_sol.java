import java.util.*;
public class Day_16_sol{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number: ");
        int a=sc.nextInt();
        Day_16_sol obj=new Day_16_sol();
        int f=obj.fact(a);
        System.out.println("Factorial of "+a+" is "+f);
    }
    int fact(int a){
        if(a==0||a==1){
            return 1;
        }
        else{
            return a*fact(a-1);
        }
    }
}