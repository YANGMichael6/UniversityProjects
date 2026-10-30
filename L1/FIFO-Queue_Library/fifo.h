#ifndef FIFO
#define FIFO

struct cell{
    int donnee;
    struct cell *suivant;
};

struct s_fifo{
    struct cell *first;
    struct cell *last;
};

typedef struct s_fifo fifo;

/*Crée une nouvelle file d’attente vide */
fifo new_fifo();

/* Donne 1 si la file xs est vide, 0 sinon */
int is_empty(fifo xs);

/* Donne la file d’attente obtenue en ajoutant x en
last de la file d’attente xs. */
fifo add(int x, fifo xs);

/* Donne la valeur en tête de la file d’attente.
Résultat non spécifié si la file est vide. */
int peek(fifo xs);

/* Donne la file d’attente dont la valeur de tête a été supprimée.
Si la file est vide la fonction donne la même file vide. */
fifo pop(fifo xs);

#endif