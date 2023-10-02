#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *frist = list, *second = list;

	if (list == NULL)
		return (0);

	while (frist && second && second->next)
	{
		frist = frist->next;
		second = second->next->next;
		if (frist == second)
			return (1);
	}
	return (0);
}
