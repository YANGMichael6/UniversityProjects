#ifndef ARBRES_H
#define ARBRES_H

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int numero;
	char destination[50];
	int depart; /* minutes depuis minuit */
}Train;

typedef struct noeud {
	Train train;
	int hauteur; /* sera utilise dans l’exercice 2 */
	struct noeud *fg;
	struct noeud *fd;
}Noeud;

typedef Noeud *ABR;

Noeud *creerNoeud(Train t);

void afficherArbre(ABR a, int profondeur);

void insererTrain(ABR *a, Train t);

void afficherDeparts(ABR a);

int hauteurReelle(ABR a);

Noeud *prochainTrain(ABR a, const char destination[], int heure);

void libererArbre(ABR a);

int hauteur(ABR a);

void majHauteur(ABR a);

void rotationDroite(ABR *a);

void rotationGauche(ABR *a);

void insererTrainAVL(ABR *a, Train t);

int verifierAux(ABR a, int *h);

int verifierAVL(ABR a);

#endif
