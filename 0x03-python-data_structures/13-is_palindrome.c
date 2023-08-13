#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *left = *head;
	listint_t *right;
	listint_t *ptr = *head;

	if (left == NULL)
		return (1);
	while (ptr->next)
		ptr = ptr->next;
	right = ptr;
	while (left->next != right && left != right)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		ptr = *head;
		while (ptr->next != right)
			ptr = ptr->next;
		right = ptr;
	}
	return (1);
}
