#include <stdio.h>
#include <stdlib.h>
#include "biblioLC.h"

BiblioLC* charger_n_entrees(const char *nom_fichier, int n){
    BiblioLC* b = creer_biblio();
    FILE *fic = fopen(nom_fichier, "r");
    if (fic == NULL) {
        printf("Fichier %s non trouve\n", nom_fichier);
        liberer_biblio(b);
        return NULL;
    }
    int i = 0;
    char ligne[256];
    while (fgets(ligne,256,fic)!=NULL && i < n) {
        int num;
        char titre[128];
        char auteur[128];
		if (sscanf(ligne,"%d %s %s\n",&num, titre, auteur)==3){
			inserer_en_tete(b, num, titre, auteur);
			i = i+1;
		} else{
			printf("Erreur de format");
			liberer_biblio(b);
			fclose(fic);
			return NULL;
		}      
	}
    fclose(fic);
    return b;   
}

void enregistrer_biblio(BiblioLC *b, char* nom_fichier){
	FILE *fic = fopen(nom_fichier, "w");
    if (fic == NULL) {
        printf("Probleme d'ouverture");
    }
    	LivreLC* l = b->L;
	while (l!=NULL){
		fprintf(fic,"%d %s %s\n", l->num, l->titre, l->auteur);
		l = l->suiv;
	}  
	fclose(fic);
}


void menu(){
	printf("Menu:\n");
	printf("0-Sortie\n");
	printf("1-Affichage\n");
	printf("2-Inserer ouvrage\n");
	printf("3-Recherche ouvrage par numero\n");
	printf("4-Recherche ouvrage par titre\n");
	printf("5-Recherche ouvrage par auteur\n");
	printf("6-Supprimer livre\n");
	printf("7-Fusionner deux bibliotheques\n");
	printf("8-Rechercher les doublons\n");
	printf("9-Enregistrer la biblio dans un fichier.\n");
	printf("Votre choix : ");
}

