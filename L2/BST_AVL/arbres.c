#include "arbres.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Noeud *creerNoeud(Train t){
	Noeud *noeud = malloc(sizeof(Noeud));
	if (noeud == NULL) return NULL;
	noeud->train = t;
	noeud->hauteur = 0;
	noeud->fg = NULL;
	noeud->fd = NULL;
	return noeud;
}

void afficherArbre(ABR a, int profondeur){
	if (a == NULL) return;
	afficherArbre(a->fd, profondeur + 1);
	for (int i = 0; i < profondeur; i++){
		printf("    ");
	}
	printf("%d\n", a->train.depart);
	afficherArbre (a->fg, profondeur + 1);
}

void insererTrain(ABR *a, Train t){
	if (*a == NULL){
		*a = creerNoeud(t);
		return;
	}
	if ((*a)->train.depart > t.depart){
		insererTrain(&((*a)->fg), t);
		return;
	}
	if ((*a)->train.depart < t.depart){
		insererTrain(&((*a)->fd), t);
		return;
	}	
}

void afficherDeparts(ABR a){
	if (a != NULL){
		afficherDeparts(a->fg);
		int heures = a->train.depart/60;
		int min = a->train.depart%60;
		printf("numero : %d, destination : %s, heure : %d:%d\n", a->train.numero, a->train.destination, heures, min);
		afficherDeparts(a->fd);
	}
}

int hauteurReelle(ABR a){
	if (a == NULL){
		return -1;
	}
	int hg = hauteurReelle(a->fg);
	int hd = hauteurReelle(a->fd);
	if (hg > hd){
		return 1 + hg;
	} else {
	    	return 1 + hd;
	}
}

Noeud *prochainTrain(ABR a, const char destination[], int heure){
	Noeud *res = NULL;
	if (a == NULL){
		return res;
	}
	Noeud *gauche = prochainTrain(a->fg, destination, heure);
	Noeud *droite = prochainTrain(a->fd, destination, heure);
	if (gauche != NULL){
		res = gauche;
	}
	if (strcmp(destination, a->train.destination) == 0 && a->train.depart >= heure){
		if (res == NULL || a->train.depart < res->train.depart){
			res = a;
		}
	}
	if (droite != NULL){
		if (res == NULL || droite->train.depart < res->train.depart){
			res = droite;
		}
	}
	return res;
}

void libererArbre(ABR a){
	if (a == NULL) return;
	libererArbre(a->fg);
	libererArbre(a->fd);
	free(a);
}

int hauteur(ABR a){
	if (a == NULL) return -1;
	return a->hauteur;
}

void majHauteur(ABR a){
	if (a == NULL) return;
	if (hauteur(a->fg) > hauteur(a->fd)){
		a->hauteur = 1 + hauteur(a->fg);
	} else {
		a->hauteur = 1 + hauteur(a->fd);
	}
}

void rotationDroite(ABR *a){
    if (*a == NULL || (*a)->fg == NULL) return;
    ABR r = *a;
    ABR g = r->fg;
    ABR v = g->fd;
    r->fg = v;
    g->fd = r;
    *a = g;
    majHauteur(r);
    majHauteur(g);
}

void rotationGauche(ABR *a){
    if (*a == NULL || (*a)->fd == NULL) return;
    ABR g = *a;
    ABR r = g->fd;
    ABR v = r->fg;
    g->fd = v;
    r->fg = g;
    *a = r;
    majHauteur(g);
    majHauteur(r);
}


void insererTrainAVL(ABR *a, Train t){
	if (*a == NULL){
		*a = creerNoeud(t);
	} else {
		if ((*a)->train.depart > t.depart){
			insererTrainAVL(&((*a)->fg), t);
			majHauteur(*a);
		} else {
			insererTrainAVL(&((*a)->fd), t);
			majHauteur(*a);
		}
	}
	int hfg = hauteur((*a)->fg);
	int hfd = hauteur((*a)->fd);
	if (hfg - hfd == 2){
		if (hauteur((*a)->fg) < hauteur((*a)->fd)){
			rotationGauche(&((*a)->fg));
		}
		rotationDroite(a);
	} else {
		if (hfg - hfd == -2){
			if (hauteur((*a)->fd) < hauteur((*a)->fg)){
				rotationGauche(&((*a)->fd));
			}
		rotationGauche(a);
		}
	}
}

int verifierAux(ABR a, int *h){
	int fe = hauteur(a->fg) - hauteur(a->fd);
	if (fe == -1 || fe == 0 || fe == 1){
		*h = hauteur(a);
		return 1;
	}
	return 0;
}

int verifierAVL(ABR a){
	int h;
	return verifierAux(a, &h);
}

