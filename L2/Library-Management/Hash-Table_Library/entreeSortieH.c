#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "entreeSortieH.h"

BiblioH* charger_n_entreesH(const char *nomfic, int n, int m){
	FILE *f = fopen(nomfic, "r");
	if (f == NULL){
		printf("Erreur ouverture fichier\n");
		return NULL;
	}
	BiblioH *b = creer_biblioH(m);
	int num;
	char titre[256];
	char auteur[256];
	int i = 0;
	while (i < n && fscanf(f, "%d %s %s", &num, titre, auteur) == 3){
		insererH(b, num, titre, auteur);
		i++;
	}
	fclose(f);
	return b;
}

void enregistrer_biblioH(BiblioH *b, char *nomfic){
	FILE *f = fopen(nomfic, "w");
	if (f == NULL){
		printf("Erreur ouverture fichier\n");
		return;
	}
	for (int i = 0; i < b->m; i++) {
		LivreH *l = b->T[i];
		while (l != NULL){
			fprintf(f, "%d %s %s\n", l->num, l->titre, l->auteur);
			l = l->suivant;
		}
	}
	fclose(f);
}

