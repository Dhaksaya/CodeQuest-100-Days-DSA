#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
    char input[2100];
    int sum = 0;

    printf("Enter numbers: ");
    fgets(input, sizeof(input), stdin); //read input including spaces
    
    char *token = strtok(input, " ");
    while(token != NULL){
        sum += atoi(token); //convert toekn to int and add to sum
        token = strtok(NULL, " ");
    }
    printf("Secret Code: %d\n", sum); //print final result

    return 0;
    
}