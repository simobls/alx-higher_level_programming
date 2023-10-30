#include "lists.h"

int check_cycle(listint_t *head) {

	listint_t* tortoise = head;
	listint_t* hare = head;

    if (head == NULL || head->next == NULL) {
        return (0);
    }

    while (hare != NULL && hare->next != NULL) {
        tortoise = tortoise->next;
        hare = hare->next->next;

        if (tortoise == hare) {
            return (1);
        }
    }

    return (0);
}
