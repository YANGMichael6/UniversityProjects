#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "biblioLC.h"
#include "biblioH.h"
#include "entreeSortieLC.h"
#include "entreeSortieH.h"

int main(int argc, char *argv[]){
    if (argc < 3){
        printf("Usage : %s fichier nb_lignes [H]\n", argv[0]);
        return 1;
    }
    int n = atoi(argv[2]);
    int rep;

    /*BiblioH*/
    if (argc == 4 && strcmp(argv[3], "H") == 0){
        BiblioH *b = charger_n_entreesH(argv[1], n, 1000);
        if (b == NULL)
            return 1;
        do{
       	    menu();
            if (scanf("%d", &rep) != 1){
                printf("Entree invalide\n");
                while(getchar() != '\n');
                continue;
            }
            switch(rep){
                case 1:
                    afficher_biblioH(b);
                    break;

                case 2:
                    int num;
                    char titre[256];
                    char auteur[256];
                    printf("Numero Titre Auteur : ");
                    if(scanf("%d %s %s",&num,titre,auteur)==3){
                        insererH(b,num,titre,auteur);
                    }
                    break;

                case 3:
                    int num1;
                    printf ("Veuillez écrire le numéro de l'ouvrage recherché.\n");
                    if (scanf("%d", &num1) == 1){
                        LivreH* l = rechercher_par_numH(b, num1);
                        printf("Voci le livre recherché : \n");
                        afficher_livreH(l);
                    } else {
                            printf("Erreur format\n");
                    }
                    break;

                case 4:
                    char titre1[256];
                    printf("Veuillez écrire le titre de l'ouvrage recherché.\n");
                    if (scanf("%s", titre1) == 1){
                        LivreH* l = rechercher_par_titreH(b, titre1);
                        printf("Voci le livre recherché : \n");
                        afficher_livreH(l);
                    } else {
                        printf("Erreur format\n");
                    }
                    break;

                case 5:
                    char auteur1[256];
                    printf("Veuillez écrire l'auteur des ouvrages recherchés.\n");
                    if (scanf("%s", auteur1) == 1){
                    	BiblioH* biblio = rechercher_par_auteurH(b, auteur1);
                        printf("Voici les livres de l'auteur recherché\n");
                        afficher_biblioH(biblio);
                        liberer_biblioH(biblio);
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
                        supprimer_livreH(b, num2, titre2, auteur2);
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
                            BiblioH* b2 = charger_n_entreesH(fichier, num3, 1000);
                            fusionner_biblioH(b, b2);
                            printf("Fusion faite. \n");
                        } else {
                            printf("Erreur format");
                        }
                    break;

                case 8:
                    BiblioH *d = doublonsH(b);
                    afficher_biblioH(d);
                    liberer_biblioH(d);
                    break;

                case 9:
                    char fichier1[256];
                    printf("Nom du fichier : ");
                    if(scanf("%s", fichier1)==1){
                        enregistrer_biblioH(b, fichier1);
                    }
                    break;
            }
        } while(rep != 0);
        liberer_biblioH(b);
    }

    /*BiblioLC*/

    else{
        BiblioLC *b = charger_n_entrees(argv[1], n);
        if (b == NULL)
            return 1;
        do{
            menu();
            if (scanf("%d", &rep) != 1){
                printf("Entree invalide\n");
                while(getchar() != '\n');
                continue;
            }
            switch(rep){
                case 1:
                    afficher_biblio(b);
                    break;

                case 2:
                    int num4;
                    char titre4[256];
                    char auteur4[256];
                    printf("Numero Titre Auteur : ");
                    if (scanf("%d %s %s", &num4, titre4, auteur4)==3){
                        inserer_en_tete(b, num4, titre4, auteur4);
                    }
                    break;

                case 3:
                    int num5;
                    printf("Numero : ");
                    if(scanf("%d",&num5)==1){
                        LivreLC *l = rechercher_par_num(b,num5);
                        if(l)
                            afficher_livre(l);
                        else
                            printf("Livre introuvable\n");
                    }
                    break;

                case 4:
                    char titre5[256];
                    printf("Titre : ");
                    if(scanf("%s", titre5)==1){
                        LivreLC *l = rechercher_par_titre(b, titre5);
                        if(l)
                            afficher_livre(l);
                        else
                            printf("Livre introuvable\n");
                    }
                    break;

                case 5:
                    char auteur5[256];
                    printf("Auteur : ");
                    if(scanf("%s", auteur5)==1){
                        BiblioLC *res = rechercher_par_auteur(b, auteur5);
                        afficher_biblio(res);
                        liberer_biblio(res);
                    }
                    break;

                case 6:
                    int num6;
                    char titre6[256];
                    char auteur6[256];
                    printf("Numero Titre Auteur : ");
                    if (scanf("%d %s %s", &num6, titre6, auteur6)==3){
                    	supprimer_livre(b, num6, titre6, auteur6);
                    }
                    break;

                case 7:
                    int nb;
                    char fichier7[256];
                    printf("Fichier NombreLignes : ");
                    if (scanf("%s %d", fichier7, &nb)==2){
                        BiblioLC *b2 = charger_n_entrees(fichier7, nb);
                        fusionner_bibliotheque(b, b2);
                        liberer_biblio(b2);
                    }
                    break;

                case 8:
                    BiblioLC *d = doublons(b);
                    afficher_biblio(d);
                    liberer_biblio(d);
                    break;

                case 9:
                    char fichier8[256];
                    printf("Nom du fichier : ");
                    if (scanf("%s", fichier8) == 1){
                        enregistrer_biblio(b, fichier8);
                    }
                    break;
            }
        } while(rep != 0);
        liberer_biblio(b);
    }
    printf("Merci et au revoir\n");
    return 0;
}
