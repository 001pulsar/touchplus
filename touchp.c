/*
This is just the beginning.
*/

#include <stdio.h>

int main() {
    
    // variables
    FILE *fptr;
    char filename[20];
    char content[50];
    
    
    // creating file
    printf("Enter file name: ");
    scanf("%s", filename);
    fptr = fopen(filename, "w");
    printf("\n\n%s created successfully!", filename);
    while((getchar()) != '\n');
    
    
    // writing to file
    printf("\n\nEnter texts to save: ");
    while(fgets(content, sizeof(content), stdin)) {
        fputs(content, fptr);
    }
    
    
    // ending
    fclose(fptr);
    return 0;
}

/*
Long way to go.
*/
