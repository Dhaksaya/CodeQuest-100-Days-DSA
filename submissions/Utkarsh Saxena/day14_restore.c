#include <stdio.h>
int main(){
    int i=0,j=0;
    char input[200],output[200],prev,next;
    printf("Enter input: ");
    scanf("%s", input);
    while(input[i] != '\0'){ //Stops when it hits the null terminator ('\0'), which marks the end of a string in C.
        if(input[i] != '_'){
            output[j++] = input[i]; //If the current character isn’t an underscore , just copy it to output.
        }else{
            prev = input[i-1];
            next = input[i+1];
            for(char c = prev + 1;c<next;c++){
                output[j++]=c; //This loop fills in every character between two letters in increasing ASCII order.
            }
        }
        i++;
    }
    output[j]='\0';
    printf("Output: %s\n", output); //Prints the final result.
    return 0;
}