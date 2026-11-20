#include <stdio.h>
#include <stdlib.h>
#include "biblioLC.h"
#include "entreeSortieLC.h"


int main(int argc, char** argv){
	if (argc != 3){
		printf("Usage: %s <nom du fichier.txt> <nombre de lignes>\n", argv[0]);
		return 1;
	}
	BiblioLC* b = charger_n_entrees(argv[1], atoi(argv[2]));
	int rep;
	do {
		menu();
		if (scanf("%d", &rep) != 1){
			printf("Entrée invalide\n");
			while(getchar() != '\n');
			continue;
		}
		if (rep > 10 || rep < 0){
			printf("Veuillez sélectionner un nombre correcte");
			scanf("%d", &rep);
		}
		switch(rep){
		case 1:
			printf ("Affichage : \n");
			afficher_biblio(b);
 			break;
 		case 2:
 			int num;
 			char titre[256];
 			char auteur[256];
 			printf("Veuillez ecrire le numero, le titre et l'auteur de l'ouvrage. \n");
 			/* On suppose que le titre et l’auteur ne contiennent pas d’espace*/
 			if (scanf("%d %s %s", &num, titre, auteur) == 3){
 				inserer_en_tete(b, num, titre, auteur);
 				printf( "Ajout fait. \n");
 			} else {
 				printf("Erreur format\n");
			}
 			break;
		case 3:
			int num1;
			printf ("Veuillez écrire le numéro de l'ouvrage recherché.\n");
			if (scanf("%d", &num1) == 1){
                                LivreLC* l = rechercher_par_num(b, num1);
				printf("Voci le livre recherché : \n");
				afficher_livre(l);
                        } else {
                                printf("Erreur format\n");
                        }
                        break;
		case 4:
			char titre1[256];
			printf("Veuillez écrire le titre de l'ouvrage recherché.\n");
			if (scanf("%s", titre1) == 1){
				LivreLC* l = rechercher_par_titre(b, titre1);
                                printf("Voci le livre recherché : \n");
                                afficher_livre(l);
			} else {
                                printf("Erreur format\n");
                        }
                        break;
		case 5:
			char auteur1[256];
			printf("Veuillez écrire l'auteur des ouvrages recherchés.\n");
			if (scanf("%s", auteur1) == 1){
				BiblioLC* biblio = rechercher_par_auteur(b, auteur1);
				printf("Voici les livres de l'auteur recherché");
				afficher_biblio(biblio);
				liberer_biblio(biblio);
			} else {
                                printf("Erreur format\n");
                        }
                        break;
		case 6:
			int num2;
                        char titre2[256];
                        char auteur2[256];
                        printf("Veuillez ecrire le numero, le titre et l'auteur de l'ouvrage à supprimer. \n");
                        if (scanf("%d %s %s", &num2, titre2, auteur2) == 3){
                                supprimer_livre(b, num2, titre2, auteur2);
                                printf("Suppression faite. \n");
                        } else {
                                printf("Erreur format\n");
                        }
                        break;
		case 7:
			int num3;
			char fichier[256];
			printf("Veuillez écrire la bibliothèque et son nombre de ligne à fusionner.\n");
			if (scanf("%s %d", fichier, &num3) == 2){
				BiblioLC* b2 = charger_n_entrees(fichier, num3);
				fusionner_bibliotheque(b, b2);
				printf("Fusion faite. \n");
			} else {
				printf("Erreur format");
			}
			break;
		case 8:
			printf("Voici les doublons de la bibliothèque.\n");
			BiblioLC* bdoublons = doublons(b);
			afficher_biblio(bdoublons);
			liberer_biblio(bdoublons);
                        break;
 		case 9:
			char fichier2[256];
			printf("Veuillez écrire le nom de la bibliothèque à enregistrer");
			if (scanf("%s", fichier) == 1){
				enregistrer_biblio(b, fichier2);
				printf("La bibliothèque a été enregistrée");
			} else {
				printf("Erreur format\n");
			}
			break;
		}
	} while (rep != 0);
  	printf("Merci, et au revoir.\n");
 	liberer_biblio(b);
	return 0;
}

