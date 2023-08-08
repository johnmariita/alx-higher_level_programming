#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a node to a sorted list
 * @head: the head of the list
 * @number: the value we're comparing to others in the list
 * Return: returns the address of the list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}
	while (ptr->next)
	{
		if (ptr->n < number && ptr->next->n > number)
		{
			new_node->next = ptr->next;
			ptr->next = new_node;
			return (*head);
		}
		ptr = ptr->next;
	}
	ptr->next = new_node;
	return (*head);
}
