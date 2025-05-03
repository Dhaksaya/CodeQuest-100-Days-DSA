#include <stdio.h>
int main(){
    int num, fact=1;
    printf("Enter a number: ");//taking input
    scanf("%d", &num);

    for(int i=1;i<=num;i++){
        fact *= i; //calculating factorial
    }
    printf("Factroial of %d is %d",num, fact); //printing final result
   return 0;
}