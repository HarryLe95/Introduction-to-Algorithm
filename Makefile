all: insertion_prog merge_prog

merge_prog: merge_sort.o utils.o
	gcc -o merge_prog merge_sort.o utils.o 

merge_sort.o: merge_sort.c
	gcc -c merge_sort.c

insertion_prog: insertion_sort.o utils.o
	gcc -o insertion_prog insertion_sort.o utils.o 

utils.o: utils.c
	gcc -c utils.c

insertion_sort.o: insertion_sort.c
	gcc -c insertion_sort.c

clean: 
	rm -f insertion_prog insertion_sort.o utils.o merge_prog merge_sort.o
	clear