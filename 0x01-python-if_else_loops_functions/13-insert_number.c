#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 *
 * @head: the pointer to the head of the list
 * @number: the number to insert
 *
 * Return: the address of the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	current = *head;
	if (!current)
	{
		new->next = NULL;
		current = new;
		return (new);
	}
	while (current->n < number && current->next)
		current = current->next;
	new->next = current->next;
	if (current->n > number)
		current = new;
	else
		current->next = new;
	return (new);
}
