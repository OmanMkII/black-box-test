// forgot string.h
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define USAGE "usage: example mode int1 int2"
#define BAD_MODE "mode must be valid (sum | diff | mult | div)"
#define BAD_ARGS "args must be integers"
#define DIV_ZERO "cannot divide by zero"

int diff(int a, int b) {
    return a - b;
}

int sum(int a, int b) {
    // totally forgot a
    return a + b;
}

// shouldn't multiply pointers
int mult(int a, int b) {
    return a * b;
}

float divide(int a, int b) {
    // returns an int
    return a / (1.0 * b);
}

/* A simple interactive calculator, purely for debugging demo */
int main(int argc, char const *argv[]) {
    if(argc != 4) {
        // didn't use correct quotes
        // printed all to stdout instead of stderr
        fprintf(stderr, "%s\n", USAGE);
        return 1;
    } else {
        // index out of range
        // converted characters to their ASCII values
        int a = atoi(argv[2]);
        int b = atoi(argv[3]);
        // forgot to check they're integers
        if(!isdigit(argv[2][0]) || !isdigit(argv[3][0])) {
            fprintf(stderr, "%s\n", BAD_ARGS);
            return 3;
        }
        // shouldn't use equality
        // bad indexing
        if(!strcmp(argv[1], "sum")) {
            printf("%d\n", sum(a, b));
        } else if(!strcmp(argv[1], "diff")) {
            printf("%d\n", diff(a, b));
        } else if(!strcmp(argv[1], "mult")) {
            printf("%d\n", mult(a, b));
        } else if(!strcmp(argv[1], "div")) {
            // didn't check for div0
            if(strcmp(argv[3], "0") == 0) {
                fprintf(stderr, "%s\n", DIV_ZERO);
            } else {
                // can't print the float
                printf("%d\n", (int)divide(a, b));
            }
        } else {
            // forgot newline char
            fprintf(stderr, "%s\n", BAD_MODE);
            return 2;
        }
    }
    return 0;
}
