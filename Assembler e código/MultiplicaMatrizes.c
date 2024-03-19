#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAMANHO 4

void print_matriz(int matriz[][TAMANHO], int tamanho);

int main() {

    srand(time(NULL));

    int a[TAMANHO][TAMANHO];
    int b[TAMANHO][TAMANHO];
    int c[TAMANHO][TAMANHO];

    for(int i = 0; i < TAMANHO; i++) {

        for(int j = 0; j < TAMANHO; j++) {

            a[i][j] = rand() % 128;
            b[i][j] = rand() % 128;

        }

    }

    for(int i = 0; i < TAMANHO; i++) {

        for(int j = 0; j < TAMANHO; j++) {

            int produto = 0;
            for(int k = 0; k < TAMANHO; k++)
                produto += a[i][k] * b[k][j];

            c[i][j] = produto;

        }

    }

    print_matriz(a, TAMANHO);
    puts("\n");
    print_matriz(b, TAMANHO);
    puts("\n");
    print_matriz(c, TAMANHO);

    return 0;
}

void print_matriz(int matriz[][TAMANHO], int tamanho) {

    for(int i = 0; i < tamanho; i++) {

        for(int j = 0; j < TAMANHO; j++)
            printf("%d ", matriz[i][j]);

        puts("");

    }

}