#ifndef entreeSortieH_h
#define entreeSortieH_h
#include <stdio.h>
#include <stdlib.h>
#include "biblioH.h"

BiblioH* charger_n_entreesH(const char *nom_fichier, int n, int m);

void enregistrer_biblioH(BiblioH *b, char* nomfic);

#endif
