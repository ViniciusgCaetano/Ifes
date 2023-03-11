#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE* ptr;
    char ch;
    // Opening file in reading mode
    ptr = fopen("mclaren.pgm", "r");
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 
    int MAX_LEN = 10000;
    char buf[] = "";


 
   
    do {
        ch = fgetc(ptr);
        if(ch == '\n'){
            printf("olha a quebra de linha!");
       }
       printf("%c", ch);
       
    } while (ch != EOF);
 
    // Closing the file
    fclose(ptr);

    return 0;
}

