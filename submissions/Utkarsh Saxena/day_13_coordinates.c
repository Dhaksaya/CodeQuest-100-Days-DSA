#include <stdio.h>
int main(){
    int digit,N,EvenDigit=0;
    printf("Enter a number: "); //taking input from the user
    scanf("%d", &N);
     printf("Even Digit: ");
     while(N>0){
        digit = N%10;
    if(digit%2 == 0){
        printf("%d ", digit); //condition to seperate each number and check whether it's even or not
        EvenDigit=1;
    }  
    N /= 10;
  }
  if(EvenDigit == 0){
    printf("No Even Digits found");// printing the result if no even number
  }
  return 0;
}