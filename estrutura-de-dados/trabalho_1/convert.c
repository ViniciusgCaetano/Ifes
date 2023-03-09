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
 
    int MAX_LEN = 300;
    char buf[] = "";


    while (fgets(buf, MAX_LEN - 1, ptr))
    {
        printf("%s", buf);
    }   

 
    // Printing what is written in file
    // character by character using loop.
    // do {
    //     ch = fgetc(ptr);
    //     if(ch == '\n'){
    //         printf("olha a quebra de linha!");
    //     }
    //     printf("%c", ch);
 
    //     // Checking if character is not EOF.
    //     // If it is EOF stop reading.
    // } while (ch != EOF);
 
    // Closing the file
    fclose(ptr);

    return 0;
}

