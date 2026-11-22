// UL2IN006 - TP6 : tests des ABR et AVL.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "arbres.h"

#define NB_TRAINS 7
#define NB_ESSAIS 10

static const Train trains[NB_TRAINS] = {
    {101, "Lyon",       510},
    {102, "Lille",      465},
    {103, "Bordeaux",   615},
    {104, "Lyon",       430},
    {105, "Rennes",     540},
    {106, "Lyon",       680},
    {107, "Strasbourg", 480}
};

static void afficherResultatRecherche(ABR arbre, const char *destination,
                                     int heure, int numeroAttendu) {
    Noeud *resultat = prochainTrain(arbre, destination, heure);
    int numeroObtenu = (resultat == NULL) ? -1 : resultat->train.numero;
    printf("  %-11s a partir de %02d:%02d : ",
           destination, heure / 60, heure % 60);
    if (resultat == NULL)
        printf("aucun train");
    else
        printf("train %d (%02d:%02d)", numeroObtenu,
               resultat->train.depart / 60, resultat->train.depart % 60);
    printf(" -- %s\n", numeroObtenu == numeroAttendu ? "OK" : "ERREUR");
}

static void testerABR(void) {
    ABR a = NULL;
    printf("\n=== EXERCICE 1 : ABR ===\n");

    for (int i = 0; i < NB_TRAINS; i++)
        insererTrain(&a, trains[i]);

    printf("\nForme de l'arbre (tourne de 90 degres) :\n");
    afficherArbre(a, 0);

    printf("\nDeparts dans l'ordre chronologique :\n");
    afficherDeparts(a);

    printf("\nHauteur reelle : %d (attendu : 2)\n", hauteurReelle(a));

    printf("\nRecherche du prochain train :\n");
    afficherResultatRecherche(a, "Lyon", 480, 101);
    afficherResultatRecherche(a, "Lyon", 540, 106);
    afficherResultatRecherche(a, "Lille", 480, -1);
    afficherResultatRecherche(a, "Bordeaux", 540, 103);
    afficherResultatRecherche(a, "Lyon", 430, 104);
    afficherResultatRecherche(a, "Lyon", 700, -1);

    /* Un doublon d'heure ne doit pas creer de nouveau noeud. */
    Train doublon = {999, "Test", 510};
    insererTrain(&a, doublon);
    printf("\nApres insertion d'un doublon d'heure, hauteur : %d (attendu : 2)\n",
           hauteurReelle(a));

    libererArbre(a);
}




/* Un essai : memes cles et meme ordre pour les deux structures. */
static void mesurer(const int cles[], int n, int *hABR, int *hAVL) {
    ABR abr = NULL;
    ABR avl = NULL;

    for (int i = 0; i < n; i++) {
        Train t = {0};
        t.numero = cles[i];
        t.depart = cles[i];  /* Cle fictive, pas forcement une heure reelle. */
        strcpy(t.destination, "Test");
        insererTrain(&abr, t);
        insererTrainAVL(&avl, t);
    }

    /* Mesure identique pour les deux structures, sans lire le champ hauteur. */
    *hABR = hauteurReelle(abr);
    *hAVL = hauteurReelle(avl);

    libererArbre(abr);
    libererArbre(avl);
}

/* Melange de Fisher-Yates. */
static void melanger(int cles[], int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int tmp = cles[i];
        cles[i] = cles[j];
        cles[j] = tmp;
    }
}



static void comparer(int n) {
    int *cles = malloc((size_t)n * sizeof(*cles));
    if (cles == NULL) {
        fprintf(stderr, "Allocation impossible pour n=%d\n", n);
        return;
    }

    int hABR, hAVL;
    for (int i = 0; i < n; i++)
        cles[i] = i;

    mesurer(cles, n, &hABR, &hAVL);
    printf("n=%4d | croissant : ABR=%4d ; AVL=%4d\n", n, hABR, hAVL);

    double sommeABR = 0.0;
    double sommeAVL = 0.0;
    for (int essai = 0; essai < NB_ESSAIS; essai++) {
        for (int i = 0; i < n; i++)
            cles[i] = i;
        melanger(cles, n);
        mesurer(cles, n, &hABR, &hAVL);
        sommeABR += hABR;
        sommeAVL += hAVL;
    }
    printf("       | aleatoire : ABR=%5.2f ; AVL=%5.2f (moyennes sur %d essais)\n",
           sommeABR / NB_ESSAIS, sommeAVL / NB_ESSAIS, NB_ESSAIS);

    free(cles);
}

static void testerAVL(void) {
    ABR a = NULL;
    /* Ordre de depart croissant. */
    const int ordre[NB_TRAINS] = {3, 1, 6, 0, 4, 2, 5};

    printf("\n=== EXERCICE 2 : AVL ===\n");
    for (int i = 0; i < NB_TRAINS; i++)
        insererTrainAVL(&a, trains[ordre[i]]);

    printf("\nForme de l'AVL :\n");
    afficherArbre(a, 0);
    printf("\nHauteur reelle : %d (attendu : 2)\n", hauteurReelle(a));
    printf("Verification AVL : %s (attendu : valide)\n",
           verifierAVL(a) ? "valide" : "INVALIDE");
    printf("Hauteur memorisee : %d ; hauteur reelle : %d\n",
           hauteur(a), hauteurReelle(a));

    printf("\nDepart chronologiques apres rotations :\n");
    afficherDeparts(a);

    /* Verifier que l'insertion d'une cle deja presente est ignoree. */
    Train doublon = {999, "Test", 510};
    insererTrainAVL(&a, doublon);
    printf("\nVerification apres doublon : %s\n",
           verifierAVL(a) ? "valide" : "INVALIDE");

    libererArbre(a);
}

int main(void) {
	srand((unsigned int)time(NULL));
	ABR arbre = NULL;
	// Insertion des trains dans arbre ABR
	for (int i = 0; i < NB_TRAINS; i++){
		insererTrain(&arbre, trains[i]);
	}
	afficherArbre(arbre, 0);

	// Affichage de la hauteur réelle
	printf("Hauteur de l'ABR : %d\n", hauteurReelle(arbre));

	// Tests de recherche
	afficherResultatRecherche(arbre, "Lyon", 480, 101);
	afficherResultatRecherche(arbre, "Lyon", 540, 106);
	afficherResultatRecherche(arbre, "Lille", 480, -1);
	afficherResultatRecherche(arbre, "Bordeaux", 540, 103);
	libererArbre(arbre);
	
	testerABR();
	testerAVL();
	
	ABR arbre2 = NULL;

	// Insertion des trains dans arbre2 AVL
	for (int i = 0; i < NB_TRAINS; i++){
		insererTrainAVL(&arbre2, trains[i]);
	}

	// Test AVL de arbre2
	int h;
	if (verifierAux(arbre2, &h)){
		printf("arbres2 est bien un AVL et sa hauteur est de %d\n", h);
	}

	afficherArbre(arbre, 0);	
		
	libererArbre(arbre);

	printf("\n=== COMPARAISON EXPERIMENTALE ===\n");
	comparer(100);
	comparer(500);
	comparer(1000);
	
	// On observe que l'insertion de nombres de façon croissante dans un ABR classique produit en quelque sorte une simple liste chainée sans sous-arbres gauches, d'où sa hauteur correspondant à n-1. A contrario, l'insertion dans un AVL produit des arbres de hauteur très minimes, ce qui correspond plus à même à une structure d'arbre.
	
	// Avec de l'aléatoire, cela permet aux ABR classique d'avoir un sens quant à leur utilisation, mais on observe toujours que les AVL ont des hauteurs plus faibles.
	
	// En effet, plus la hauteur d'un arbre est petite, plus les fonctions de recherche et de suppression sont moins couteuse puisque leur complexité dépendent de la hauteur (elles sont en O(h = log(n))). A noter que pour des ABR non équilibré, ces fonctions sont en O(h = n) dans le pire des cas. Donc les AVL ont une meilleure complexité que les ABR classiques si l'on veut rechercher ou supprimer un élément de l'arbre.
	
	// Cependant, pour ce qui est de notre fonction prochainDepart(), le fait que l'on utilise un AVL n'améliore pas forcément sa complexité. En effet, la fonction doit impérativement parcourir toutes les branches de l'arbres pour trouver surtout la destination puisque l'AVL n'est pas seulement construite selon les heures de départ.
	return 0;
}
