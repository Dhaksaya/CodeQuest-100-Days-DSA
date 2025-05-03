import java.util.*;
public class Day_13_sol{
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        int n;
        System.out.print("Enter N: ");
        n=sc.nextInt();
        int d,i=n,c=0;
        while(i!=0){
            d=i%10;
            if(d%2==0){
                c++;
            }
            i=i/10;
        }
        i=n;
        int j=0;
        if(c>0){
            int arr[]=new int[c];
            while(i!=0){
                d=i%10;
                if(d%2==0){
                    arr[j++]=d;
                }
                i=i/10;
            }
            System.out.print("Even digits: ");
            for( i = c-1; i >= 0; i--) {
                System.out.print(arr[i]+" ");
            }
        }
        else{
            System.out.println("No even digits found!");
        }
    }
}