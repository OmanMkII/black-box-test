// forgot string.h
#include <stdio.h>

#define USAGE "usage: example mode int1 int2"
#define BAD_MODE "mode must be valid (sum | diff | mult | div)"
#define BAD_ARGS "args must be integers"
#define DIV_ZERO "cannot divide by zero"

int diff(int a, int b) {
    // forgot a semi-colon
    return a - b;
    // return a - b
}

int sum(int a, int b) {
    // totally forgot a
    return b;
}

// shouldn't multiply pointers
int mult(int* a, int* b) {
    return (int)a * (int)b;
}

float divide(int a, int b) {
    // returns a casted int
    return (float) a / b;
}

/* A simple interactive calculator, purely for debugging demo. Warnings have been
 * ignored by the makefile to make problems a little harder to spot.
 */
int main(int argc, char const *argv[]) {
    if(argc != 4) {
        // didn't use correct quotes
        printf('%s\n', USAGE);
        return 1;
    } else {
        // index out of range
        // converted characters to their ASCII values
        int a = (int)argv[3];
        int b = (int)argv[4];
        // forgot to check they're integers
        // shouldn't use equality
        // bad indexing
        if(argv[2] == "sum") {
            printf("%d\n", sum(a, b));
        } else if(argv[2] == "diff") {
            printf("%d\n", diff(a, b));
        } else if(argv[2] == "mult") {
            printf("%d\n", mult(a, b));
        } else if(argv[2] == "div") {
            // can't print a float
            printf("%d\n", divide(a, b));
        } else {
            // forgot newline char
            printf(BAD_MODE);
        }
    }
    // left the else without a return
    return 0;
}
