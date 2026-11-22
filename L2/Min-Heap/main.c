#include <stdlib.h>
#include <stdio.h>
#include "tas.h"

int main(){
	Tas *tas = creerTas(10);
	Tache sauvegarde = {1, "sauvegarde", 5};
	Tache antivirus = {2, "antivirus", 2};
	Tache impression = {3, "impression", 8};
	Tache miseajour = {4, "miseajour", 4};
	Tache alerte = {5, "alerte", 1};
	ajouter(tas, sauvegarde);
	ajouter(tas, antivirus);
	ajouter(tas, impression);
	ajouter(tas, miseajour);
	ajouter(tas, alerte);
	afficherTas(tas);
	
	Tache min;
	
	extraireMin(tas, &min);
	printf("extraite : id = %d priorite = %d\n", min.id, min.priorite);
	extraireMin(tas, &min);
	printf("extraite : id = %d priorite = %d\n", min.id, min.priorite);
	extraireMin(tas, &min);
	printf("extraite : id = %d priorite = %d\n", min.id, min.priorite);
	extraireMin(tas, &min);
	printf("extraite : id = %d priorite = %d\n", min.id, min.priorite);
	afficherTas(tas);
	extraireMin(tas, &min);
	printf("extraite : id = %d priorite = %d\n", min.id, min.priorite);
	afficherTas(tas);
	extraireMin(tas, &min);
	printf("extraite : id = %d priorite = %d\n", min.id, min.priorite); // la valeur de min est celle de la précédente
	afficherTas(tas);
	
	libererTas(tas);
	
	printf("-----------------------\n");
	
	Tache tab[5] = { {1, "sauvegarde", 5}, {2, "antivirus", 2}, {3, "impression", 8}, {4, "miseajour", 4}, {5, "alerte", 1} };
	trierTaches(tab, 5);
	
	for (int i = 0; i < 5; i++){
		printf("%d\n", tab[i].priorite);
	}
	
	printf("-----------------------\n");
	
	Tache tab2[5] = { {1, "sauvegarde", 5}, {2, "antivirus", 2}, {3, "impression", 8}, {4, "miseajour", 4}, {5, "alerte", 1} };
	Tas *tas2 = creerTas(5);
	construireTas(tas2, tab2, 5);
	afficherTas(tas2);
	libererTas(tas2);
	
	printf("-----------------------\n");
	
	Tache tab3[5] = { {1, "sauvegarde", 5}, {2, "antivirus", 2}, {3, "impression", 8}, {4, "miseajour", 4}, {5, "alerte", 1} };
	trierTaches2(tab3, 5);
	for (int i = 0; i < 5; i++){
		printf("%d\n", tab3[i].priorite);
	}
	
	/* trierTas() et trierTas2() ont théoriquement la même complexité temporelle qui est de O(nlog(n)), avec n le nombre de Taches du tas. Cependant, la différence est que lors de la construction du tas auxiliaire, construireTas() est en O(n) au lieu de O(nlog(n)) pour trierTas() à cause de ajouter() qui est en O(log(n)) et dans une boucle à n itérations. Donc au final, trierTas2() est à priori meilleure en terme de complexité en pratique à cause de la construction du tas. Pour la complexité spatiale, ils sont tous deux en O(n), qui correspond aux malloc sur la taille des tableaux du tas.*/

	return 0;
}


