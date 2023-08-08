#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast && slow && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return 1;
	}
	return 0;
}
