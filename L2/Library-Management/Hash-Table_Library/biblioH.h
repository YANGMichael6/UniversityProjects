#ifndef biblioH_h
#define biblioH_h
#include <stdio.h>
#include <stdlib.h>

typedef struct livreh{
	int clef;
	int num;
	char * titre;
	char * auteur;
	struct livreh *suivant;
} LivreH;

typedef struct table{
	int nE;
	int m;
	LivreH **T;
} BiblioH;

int fonctionClef(char* auteur);

LivreH* creer_livreH(int num, char* titre, char* auteur);

void liberer_livreH(LivreH* l);

BiblioH* creer_biblioH(int m);

void liberer_biblioH(BiblioH* b);

int fonctionHachage(int cle, int m);

void insererH(BiblioH* b, int num, char* titre, char* auteur);

LivreH *rechercher_par_numH(BiblioH *b, int num);

BiblioH* rechercher_par_auteurH(BiblioH* b, char* auteur);

LivreH* rechercher_par_titreH(BiblioH* b, char* titre);

BiblioH *doublonsH(BiblioH *b);

void afficher_livreH(LivreH *l);

void afficher_biblioH(BiblioH *b);

void fusionner_biblioH(BiblioH *b1, BiblioH *b2);

void supprimer_livreH(BiblioH *b, int num, char *titre, char *auteur);

#endif
