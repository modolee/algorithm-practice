#include <stdio.h>

int main() {
    int dayDigit;
    int carCount[10] = {0,};
    int i, temp;

    scanf("%d", &dayDigit);
    for (i = 0; i < 5; i++) {
        scanf("%d", &temp);
        carCount[temp-1]++;
    }

    printf("%d", carCount[dayDigit-1]);
}