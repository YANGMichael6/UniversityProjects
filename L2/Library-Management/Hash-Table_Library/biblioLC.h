#ifndef biblioLC
#define biblioLC

#include <stdio.h>
#include <stdlib.h>

typedef struct livre {
	int num ;
	char * titre ;
	char * auteur ;
	struct livre * suiv ;
} LivreLC ;

typedef struct { /* Tete fictive */
	LivreLC * L ; /* Premier element */
} BiblioLC ;

LivreLC* creer_livre(int num, char* titre, char* auteur);

void liberer_livre(LivreLC* l);

BiblioLC* creer_biblio();

void liberer_biblio(BiblioLC* b);

void inserer_en_tete(BiblioLC* b,int num,char* titre,char* auteur);

void afficher_livre(LivreLC* l);

void afficher_biblio(BiblioLC* b);

LivreLC* rechercher_par_num(BiblioLC* b, int num);

LivreLC* rechercher_par_titre(BiblioLC* b, char* titre); 

BiblioLC* rechercher_par_auteur(BiblioLC* b, char* auteur);

void supprimer_livre(BiblioLC* b, int num, char* titre, char* auteur);

void fusionner_bibliotheque(BiblioLC* b1, BiblioLC* b2);

BiblioLC* doublons(BiblioLC* b);

#endif
