#include "lists.h"

int is_palindrome(listint_t **head)
{
    if (!head || !(*head) || !((*head)->next))
        return (1); // An empty list or a list with a single node is considered a palindrome

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    
    // Use Floyd's cycle-finding algorithm to find the middle of the list
    while (fast && fast->next)
    {
        fast = fast->next->next;
        listint_t *temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    if (fast)  // If the list has an odd number of nodes, skip the middle node
        slow = slow->next;

    // Compare the first half and the reversed second half of the list
    while (slow)
    {
        if (slow->n != prev->n)
            return (0); // Not a palindrome
        slow = slow->next;
        prev = prev->next;
    }
    
    return (1); // It's a palindrome
}
