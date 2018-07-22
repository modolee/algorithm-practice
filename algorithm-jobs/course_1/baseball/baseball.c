#include <stdio.h>
#include <stdlib.h>

#define STRIKE 0
#define BALL 1

int **ansSheet;
int **strikeOrBall;
int numOfAnsSheet;

int * slice(int digits) {
    int *slicedDigits;
    slicedDigits = (int *)malloc(sizeof(int) * 3);
    slicedDigits[0] = digits % 10;
    slicedDigits[1] = digits / 10 % 10;
    slicedDigits[2] = digits / 100;

    return slicedDigits;
}

int is_valid(int *candidate) {
   if(candidate[0] != candidate[1]) {
       if(candidate[0] != candidate[2]) {
           if(candidate[1] != candidate[2]) {
               return 1;
           }
       }
   }
   return 0;
}

int check_answer(int *candidate) {
    int i, j, k;
    int strike, ball;
    int pass = 1;
    
    for(i = 0; i < numOfAnsSheet; i++) {
		strike = 0;
		ball = 0;
        for(j = 0; j < 3; j++) {
            for(k = 0; k < 3; k++) {
                if(candidate[j] == ansSheet[i][k]) {
                    if (j == k) {
                        strike++;
                    } else {
                        ball++;
                    }
					break;
                }
            }
        }
        if(strikeOrBall[i][STRIKE] != strike || strikeOrBall[i][BALL] != ball) {
            pass = 0;
            return pass;
        }
    }
    return pass;
}

int main() {
    int try;
    int strike;
    int ball;
    int i;
    int *candidate;
    int pass = 0;

    scanf("%d", &numOfAnsSheet);

    ansSheet = (int **)malloc(sizeof(int *) * numOfAnsSheet);
    strikeOrBall = (int **)malloc(sizeof(int *) * numOfAnsSheet);
    
    for(i = 0; i < numOfAnsSheet; i++) {
        strikeOrBall[i] = (int *)malloc(sizeof(int) * 2);
        
        scanf("%d %d %d", &try, &strike, &ball);
    
        ansSheet[i] = slice(try);
        strikeOrBall[i][STRIKE] = strike;
        strikeOrBall[i][BALL] = ball;
    }

    for(i = 123; i <= 987; i++) {
        candidate = slice(i);
        if(!is_valid(candidate)) {
            continue;
        } else {
            pass += check_answer(candidate);
        }
    }

    printf("%d", pass);
}