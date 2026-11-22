#include "tas.h"
#include <stdio.h>
#include <stdlib.h>

Tas *creerTas(int capacite){
	Tas *tas = malloc(sizeof(Tas));
	tas->capacite = capacite;
	tas->tab = malloc(sizeof(Tache) * tas->capacite);
	tas->taille = 0;
	return tas;
}

void libererTas(Tas *t){
	if (t != NULL){
		free(t->tab);
		free(t);
	}
}

void afficherTas(Tas *t){
	if (t == NULL){
		return;
	}
	if (t->taille == 0){
		printf("tas vide\n");
	}
	for (int i = 1; i <= t->taille; i++){
		printf("(%d %s %d)\n", t->tab[i].id, t->tab[i].nom, t->tab[i].priorite);
	}
}

void echanger(Tas *t, int i, int j){
	if (t == NULL || i > t->taille || j > t->taille) return;
	Tache tmp = t->tab[i];
	t->tab[i] = t->tab[j];
	t->tab[j] = tmp;
}

void monter(Tas *t, int i){
	if (t == NULL || i > t->taille) return;
	if (i/2 != 0 && t->tab[i/2].priorite > t->tab[i].priorite){
		echanger(t, i/2, i);
		monter(t, i/2);
	}
}

int ajouter(Tas *t, Tache x){
	if (t->taille == t->capacite) return 0;
	t->taille++;
	t->tab[t->taille] = x;
	monter(t, t->taille);
	return 1;
}

int rechercherMin(Tas *t, Tache *res){
	if (t == NULL || t->taille == 0) return 0;
	*res = t->tab[1];
	return 1;
}

void descendre(Tas *t, int i){
    if (t == NULL || i > t->taille) return;
    int gauche = 2 * i;
    int droite = 2 * i + 1;
    int min = i;
    if (gauche <= t->taille && t->tab[gauche].priorite < t->tab[min].priorite){
        min = gauche;
    }
    if (droite <= t->taille && t->tab[droite].priorite < t->tab[min].priorite){
        min = droite;
    }
    if (min != i){
        echanger(t, i, min);
        descendre(t, min);
    }
}

int extraireMin(Tas *t, Tache *res){
	if (t == NULL || t->taille == 0) return 0;
	rechercherMin(t, res);
	t->tab[1] = t->tab[t->taille];
	t->taille--;	
	if (t->taille > 0){
        	descendre(t, 1);
        }
	return 1;
}


void trierTaches(Tache* tab, int n){
	Tas *tas = creerTas(n);
	for (int i = 0; i < n; i++){
		ajouter(tas, tab[i]);
	}
	Tache min;
	for (int i = 0; i < n; i++){
		extraireMin(tas, &min);
		tab[i] = min;
	}
	libererTas(tas);
}

void construireTas(Tas *t, Tache tab[], int n){
	for (int i = 1; i <= n; i++){
		t->tab[i] = tab[i-1];
	}
	t->taille = n;
	for (int i = t->taille / 2; i >= 1; i--){
		descendre(t, i);
	}
}

void trierTaches2(Tache *tab, int n){
	Tas *tas = creerTas(n);
	construireTas(tas, tab, n);
	Tache min;
	for (int i = 0; i < n; i++){
		extraireMin(tas, &min);
		tab[i] = min;
	}
	libererTas(tas);	
}


