#ifndef TAS_H
#define TAS_H

#include <stdio.h>
#include <stdlib.h>

#define TAILLE_NOM 40

typedef struct {
	int id;
	char nom[TAILLE_NOM];
	int priorite;
}Tache;

typedef struct {
	int capacite; /* nombre maximum de taches */
	int taille; /* nombre de taches presentes */
	Tache *tab; /* tableau de capacite + 1 cases */
}Tas; 

Tas *creerTas(int capacite);

void libererTas(Tas *t);

void afficherTas(Tas *t);

void echanger(Tas *t, int i, int j);

void monter(Tas *t, int i);

int ajouter(Tas *t, Tache x);

int rechercherMin(Tas *t, Tache *res);

void descendre(Tas *t, int i);

int extraireMin(Tas *t, Tache *res);

void trierTaches(Tache* tab, int n);

void construireTas(Tas *t, Tache tab[], int n);

void trierTaches2(Tache *tab, int n);

#endif
