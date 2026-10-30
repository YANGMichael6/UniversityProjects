#include <stdlib.h>
#include "fifo.h"

fifo new_fifo(){
    fifo r;
    r.first = NULL;
    r.last = NULL;
    return r;
}

int is_empty(fifo xs) {
    return (xs.first == NULL && xs.last == NULL);
}

fifo add(int x, fifo xs){
    struct cell *c = malloc(sizeof(struct cell));
    c->donnee = x; c->suivant = NULL;
    if (is_empty(xs)){
        xs.first = c; xs.last = c;
    }
    else{
        xs.last->suivant = c; xs.last = c;
    }
    return xs;
    }

int peek(fifo xs){ 
        return xs.first->donnee;
}

fifo pop(fifo xs){
    if (!is_empty(xs)){
        struct cell *d = xs.first;
        xs.first = xs.first->suivant; free(d);
        if (xs.first == NULL) xs.last = NULL;
    }
    return xs;
}

