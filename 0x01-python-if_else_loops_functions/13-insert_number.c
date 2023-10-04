#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	if (head == NULL)
		return (NULL);
	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next && temp->next->n < number)
		temp = temp->next;
	new->next = temp->next;
	temp->next = new;
	return (new);
}
