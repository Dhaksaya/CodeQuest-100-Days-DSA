#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(){
    char pswd[400];
    int upper=0,lower=0,digit=0,special=0;

printf("Enter a password ");
scanf("%s", pswd);// taking user input
    if(strlen(pswd)<8){
        printf("Weak password");//checking first condition
        return 0;
    }
    for(int i=0; i<strlen(pswd); i++){
        if(isupper(pswd[i]))
        upper=1;
        else if(islower(pswd[i]))
        lower=1;
        else if(isdigit(pswd[i]))
        digit=1;
        else
        special=1; //checking all next conditions
    }
    if(upper && lower && digit && special){
        printf("Strong password");
    }else{
        printf("Weak password"); //final output
    }
    return 0;
}