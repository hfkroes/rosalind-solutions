#include <stdio.h>
#include <string.h>

int main() {

    char dna[1000];
    FILE *input;    
    input = fopen("D:/_Hector/C", "r");
    fgets(dna, 1000, input);
    fclose(input);

    int i;
    int a = 0;
    int c = 0;
    int g = 0;
    int t = 0;
    for(i=0; i<strlen(dna); i++) {
        if (dna[i] == 'A') {
            a += 1;
        }
        else if (dna[i] == 'C') {
            c += 1;
        }
        else if (dna[i] == 'G') {
            g += 1;
        }
        else if (dna[i] == 'T') {
            t += 1;
        }
    }

    printf("%i %i %i %i", a, c, g, t);
    return 0;
}