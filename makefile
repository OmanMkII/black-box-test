# Default assembly process
.PHONY: all
.DEFAULT_GOAL: all
all: correct example

# Basic makefile structure
correct: correct.o
	gcc correct.o -o correct

correct.o:
	gcc -c -pedantic -Wall -Werror correct.c

example: example.o
	gcc example.o -o example

example.o:
	gcc -c -w example.c

# Simple clean process
.PHONY: clean
clean:
	rm *.o example correct
