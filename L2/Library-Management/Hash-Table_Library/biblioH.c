#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "biblioH.h"

int fonctionClef(char* auteur){
        int cle = 0;
        int i = 0;
        while (auteur[i]!='\0'){
                cle = cle + (int)(auteur[i]);
                i = i+1;
        }
	return cle;
}

LivreH* creer_livreH(int num, char* titre, char* auteur){
	int cle = fonctionClef(auteur);
	LivreH* l = (LivreH *) malloc(sizeof(LivreH));
	l->clef = cle;
	l->num = num;
	l->titre = strdup(titre);
	l->auteur = strdup(auteur);
	l->suivant = NULL;
	return l;
}

void liberer_livreH(LivreH* l){
	LivreH *tmp;
	while (l != NULL){
		tmp = l->suivant;
		free(l->titre);
		free(l->auteur);
		free(l);
		l = tmp;
	}
}


BiblioH* creer_biblioH(int m){
	BiblioH* b = malloc(sizeof(BiblioH));
	b->nE = 0;
	b->m = m;
	b->T = malloc(sizeof(LivreH)*m);
	return b;
}

void liberer_biblioH(BiblioH* b){
	for (int i = 0; i < b->m; i++){
		liberer_livreH(b->T[i]);
	}
}

int fonctionHachage(int cle, int m){
	float A = (sqrt(5)-1)/2;
	return (int)(m*(cle*A-(int)(cle*A)));
}

void insererH(BiblioH* b, int num, char* titre, char* auteur){
	int cle = fonctionClef(auteur);
	int ind = fonctionHachage(cle, b->m);
	LivreH* l =  creer_livreH(num, titre, auteur);
	l->suivant = b->T[ind];
	b->T[ind] = l;
}

LivreH *rechercher_par_numH(BiblioH *b, int num){
    if (b == NULL)
        return NULL;
    for (int i = 0; i < b->m; i++){
        LivreH *l = b->T[i];
        while (l != NULL){
            if (l->num == num)
                return l;
            l = l->suivant;
        }
    }
    return NULL;
}

BiblioH* rechercher_par_auteurH(BiblioH* b, char* auteur){
	BiblioH* res = creer_biblioH(b->m);
	int cle = fonctionClef(auteur);
	int i = fonctionHachage(cle, b->m);
	LivreH* l = b->T[i];
	while (l != NULL) {
		if (strcmp(l->auteur, auteur) == 0){
			insererH(res, l->num, l->titre, l->auteur);
		}
		l = l->suivant;
	}
	return res;
}

LivreH* rechercher_par_titreH(BiblioH* b, char* titre){
	for (int i = 0; i < b->m; i++){
		LivreH* l = b->T[i];
		while (l != NULL){
			if (strcmp(l->titre, titre) == 0){
				return l;
			}
		l = l->suivant;
		}
	}
	return NULL;
}

BiblioH *doublonsH(BiblioH *b){
    if (b == NULL) return NULL;
    BiblioH *res = creer_biblioH(b->m);
    for (int i = 0; i < b->m; i++){
        LivreH *l = b->T[i];
        while (l != NULL){
            BiblioH *bauteur = rechercher_par_auteurH(b, l->auteur);
            int trouve = 0;
            for (int j = 0; j < bauteur->m && !trouve; j++){
                LivreH *cour = bauteur->T[j];
                while (cour != NULL && !trouve){
                    if (cour->num != l->num && strcmp(cour->titre, l->titre) == 0) trouve = 1;
                    cour = cour->suivant;
                }
            }
            if (trouve) insererH(res, l->num, l->titre, l->auteur);
            liberer_biblioH(bauteur);
            l = l->suivant;
        }
    }
    return res;
}


void afficher_livreH(LivreH *l){
	printf("%d %s %s\n", l->num, l->titre, l->auteur);
}

void afficher_biblioH(BiblioH *b){
	if (b == NULL){
		printf("Bibliothèque vide\n");
		return;
	}
	for (int i = 0; i < b->m; i++){
		LivreH *l = b->T[i];
		while (l != NULL){
			afficher_livreH(l);
			l = l->suivant;
		}
	}
}

void fusionner_biblioH(BiblioH *b1, BiblioH *b2){
    if (b1 == NULL || b2 == NULL) return;
    for (int i = 0; i < b2->m; i++){
        LivreH *l = b2->T[i];
        while (l != NULL){
            insererH(b1, l->num, l->titre,l->auteur);
            l = l->suivant;
        }
    }
}

void supprimer_livreH(BiblioH *b, int num, char *titre, char *auteur){
    if (b == NULL) return;
    int cle = fonctionClef(auteur);
    int indice = fonctionHachage(cle, b->m);
    LivreH *cour = b->T[indice];
    LivreH *prec = NULL;
    while (cour != NULL){
        if (cour->num == num && strcmp(cour->titre, titre) == 0 && strcmp(cour->auteur, auteur) == 0){
            if (prec == NULL){
                b->T[indice] = cour->suivant;
            } else {
                prec->suivant = cour->suivant;
            }
            liberer_livreH(cour);
            b->nE = b->nE - 1;
            return;
        }
        prec = cour;
        cour = cour->suivant;
    }
}
