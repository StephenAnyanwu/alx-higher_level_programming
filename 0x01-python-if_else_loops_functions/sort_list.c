#include "lists.h"
/**
* sort_list - sorts a singly linked list in ascending order.
* @head: pointer to pointer of first node of listint_t list.
*/
void sort_list(listint_t **head)
{
	listint_t *tmp = *head;
	int val;

	while ((*head)->next != NULL)
	{
		listint_t *ptr = (*head)->next;

		while (ptr->next != NULL)
		{
			if ((*head)->n > ptr->n)
			{
				val = (*head)->n;
				(*head)->n = ptr->n;
				ptr->n = val;
			}
			ptr = ptr->next;
		}
		*head = (*head)->next;
	}
	*head = tmp;

}
