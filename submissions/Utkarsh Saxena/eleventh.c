#include <stdio.h>
int main(){
    int j,temp,i,n=0;
    int arr[100];
    printf("Enter numbers: "); //taking input from user
   while(scanf("%d", &arr[n]) == 1){
    n++;
    char ch = getchar();
    if(ch == '\n') break; //attenuates after enter key pressed
   }
    for(i=0;i<n;i++){ //ascending order sort
        for(j=i+1;j<n;j++){
            if(arr[i]>arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("Sorted list: ");
    for( i=0;i<n;i++){
        printf("%d ", arr[i]); //final result
    }
    return 0;
}
