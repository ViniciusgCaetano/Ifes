# include <stdio.h>
# include <stdlib.h>
# include <time.h>
# include <unistd.h>

void main(){
    
    int user_number = 0;
    int min_number = 1;
    int max_number = 1024;

    printf("Escreva um número: ");
    scanf("%d", &user_number);

    int tentatives = 0;
    int machine_number = 0;

    do{  

        machine_number = min_number + (max_number - min_number)/2 ;
        tentatives++;
        if(machine_number > user_number){
            printf("machine number: %d\n", machine_number);
            printf("1\n");
            max_number = machine_number;

        }else{
            printf("machine number: %d\n", machine_number);
            printf("-1\n");
            min_number = machine_number;

        }
        sleep(1);
       
    }
    while(user_number != machine_number);

    printf("0 - Tentativas: %d\n", tentatives);
    printf("O número é: %d", user_number);

}
