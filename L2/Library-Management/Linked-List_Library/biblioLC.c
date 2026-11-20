#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "biblioLC.h"

LivreLC* creer_livre(int num, char* titre, char* auteur){
	LivreLC* livre = (LivreLC*)malloc(sizeof(LivreLC));
	livre->num = num;
	livre->titre = strdup(titre);
	livre->auteur = strdup(auteur);
	livre->suiv = NULL;
	return livre;
}

void liberer_livre(LivreLC* l){
	LivreLC* tmp = NULL;
	while(l != NULL) {
		tmp = l;
		l = l->suiv;
		free(tmp->titre);
		free(tmp->auteur);
		free(tmp);
	}
}

BiblioLC* creer_biblio(){
	BiblioLC* new = (BiblioLC*)malloc(sizeof(BiblioLC));
	new->L = NULL;
	return new;
}

void liberer_biblio(BiblioLC* b){
	liberer_livre(b->L);
	free(b);
}

void inserer_en_tete(BiblioLC* b,int num,char* titre,char* auteur){
	LivreLC* new = creer_livre(num, titre, auteur);
	new->suiv = b->L;
	b->L = new;
}

void afficher_livre(LivreLC* l){
	if (l != NULL){
		printf("%d %s %s \n", l->num, l->titre, l->auteur);
	}
	printf("Livre inexistant");
}

void afficher_biblio(BiblioLC* b){
	LivreLC* p = b->L;
	while (p != NULL){
		afficher_livre(p);
		p = p->suiv;
	}
}

LivreLC* rechercher_par_num(BiblioLC* b, int num){
	LivreLC* p = b->L;
	while(p != NULL){
		if (p->num == num){
			return p;
		}
		p = p->suiv;
	}
	return NULL;
}

LivreLC* rechercher_par_titre(BiblioLC* b, char* titre){
        LivreLC* p = b->L;
        while(p != NULL){
                if (strcmp(p->titre, titre) == 0){
                        return p;
                }
                p = p->suiv;
        }
	return NULL;
}

BiblioLC* rechercher_par_auteur(BiblioLC* b, char* auteur){
        LivreLC* p = b->L;
	BiblioLC* new = creer_biblio();
        while(p != NULL){
                if (strcmp(p->auteur, auteur) == 0){
                        inserer_en_tete(new, p->num, p->titre, p->auteur);
                }
                p = p->suiv;
        }
	return new;
}

void supprimer_livre(BiblioLC* b, int num, char* titre, char* auteur){
	LivreLC *p = b->L;
	LivreLC* prec = NULL;
	while(p != NULL){
	        if (p->num == num && strcmp(p->titre, titre) == 0 && strcmp(p->auteur, auteur) == 0){
                	if (prec == NULL){
				b->L = p->suiv;
			} else {
				prec->suiv = p->suiv;
			}
			free(p->titre);
			free(p->auteur);
			free(p);
			p = NULL;
		}
		prec = p;
		p = p->suiv;
	}
}

void fusionner_bibliotheque(BiblioLC* b1, BiblioLC* b2){
	if (b1->L == NULL){
		b1->L = b2->L;
		free(b2);
	}
	LivreLC *p1 = b1->L;
	while(p1->suiv != NULL){
		p1 = p1->suiv;
	}
	p1->suiv = b2->L;
	free(b2);
}

BiblioLC* doublons(BiblioLC* b){
	LivreLC* p = b->L;
	LivreLC* cherche = NULL;
        BiblioLC* new = creer_biblio();
        while(p != NULL){
		cherche = p->suiv;
		while(cherche != NULL){
	                if (strcmp(p->auteur, cherche->auteur) == 0 && strcmp(p->titre, cherche->titre) == 0){
        	                inserer_en_tete(new, p->num, p->titre, p->auteur);
			}
			cherche = cherche->suiv;
		}
                p = p->suiv;
	}
        return new;
}
