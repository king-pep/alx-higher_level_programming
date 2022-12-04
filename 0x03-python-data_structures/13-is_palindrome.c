#include "lists.h"

/**
* list_len - finds no. of elements ina linked list.
* @h: pointer to linked list.
*
* Return: number of elements in linked list.
*/
size_t list_len(listint_t *h)
{
	size_t  nodes = 0;

	if (h == NULL)
		return (0);
	while (h != NULL)
	{
		nodes++;
		h = h->next;
	}
	return (nodes);
}

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: double pointert to head of d-list.
*
* Return: 1 if palindrome, 0 otherwise.
*/
size_t list_len(const listint_t *h)
{
    size_t i = 0;

    while (h)
    {
        i++;
        h = h->next;
    }
    return (i);
}
