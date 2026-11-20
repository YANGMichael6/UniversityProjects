all : main

main : main.o biblioLC.o entreeSortieLC.o biblioH.o entreeSortieH.o
	gcc -o main main.o biblioLC.o entreeSortieLC.o biblioH.o entreeSortieH.o

main.o : main.c biblioLC.h entreeSortieLC.h biblioH.h entreeSortieH.h
	gcc -c main.c

entreeSortieLC.o : entreeSortieLC.c entreeSortieLC.h biblioLC.h
	gcc -c entreeSortieLC.c

BiblioLC.o : biblioLC.c biblioLC.h
	gcc -c BiblioLC.c

entreeSortieH.o : entreeSortieH.c entreeSortieH.h biblioH.h
	gcc -c entreeSortieH.c

BiblioH.o : biblioH.c biblioH.h
	gcc -c biblioH.c

clean :
	rm -f main *.o
