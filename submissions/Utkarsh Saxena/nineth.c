#include <stdio.h>
#include <string.h>
int main(){
    char str[200]; //defining string
    printf("Enter a string");
    scanf("%[^\n]", str); //taking input from the user
    int len = strlen(str); //taking length of string
    printf("Reversed string: "); //printing the final result
    for(int i=len-1;i>=0;i--){
        putchar(str[i]);
    }
    return 0;
}
