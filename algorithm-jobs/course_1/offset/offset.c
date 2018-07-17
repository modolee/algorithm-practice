#include <stdio.h>

#define NUM_DIGITS 5

int main() {
    int inputArray[NUM_DIGITS][NUM_DIGITS];
    int outputArray[NUM_DIGITS][NUM_DIGITS];
    int i, j, k, l;
    int direction[4][2];
    int smallerThanMe;

    for(i = 0; i < NUM_DIGITS; i++) {
        for(j = 0; j < NUM_DIGITS; j++) {
            scanf("%d", &inputArray[i][j]);
        }
    }

    for(i = 0; i < NUM_DIGITS; i++) {
        for(j = 0; j < NUM_DIGITS; j++) {
            // 상
            direction[0][0] = i - 1;
            direction[0][1] = j;

            // 하
            direction[1][0] = i + 1;
            direction[1][1] = j;

            // 좌
            direction[2][0] = i;
            direction[2][1] = j - 1;

            // 우
            direction[3][0] = i;
            direction[3][1] = j + 1;

            for(k = 0, smallerThanMe = 0; k < 4; k++) {
                if( (direction[k][0] < NUM_DIGITS && direction[k][0] >= 0) 
                    && (direction[k][1] < NUM_DIGITS && direction[k][1] >= 0) 
                    && inputArray[direction[k][0]][direction[k][1]] <=  inputArray[i][j]) {
                        smallerThanMe = 1;
                        break;
                }
            }
            if(smallerThanMe) {
                printf("%d ", inputArray[i][j]);
            } else {
                printf("%c ", '*');
            }
        }
        printf("\n");
    }
}