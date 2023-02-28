# include <stdio.h>
# include <stdlib.h>
# include <time.h>

void main(){
    srand(time(NULL));
    int random_number = rand() % (1024) + 1;
    int user_number = 0;
    int tentatives = 0;
    do{  
        printf("Escreva um número: ");
        scanf("%d", &user_number);
        if(user_number > random_number){
            printf("%d\n", 1);
        } else{
            printf("%d\n", -1);
        }
        tentatives++;
    }
    
    while(user_number != random_number);

    printf("0 - Tentatives %d\n", tentatives);
    printf("O número é: %d", random_number);

}
