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

/**
* insert_node - a function that inserts a number into a
* sorted singly linked list.
* @head: pointer to pointer of first node of listint_t list
* @number: number to insert into list
* Return: address of the new element or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *ptr1, *ptr2;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	sort_list(head);
	ptr1 = *head;
	ptr2 = (*head)->next;
	while (ptr2 != NULL)
	{
		if (ptr2->n > new->n)
		{
			ptr1->next = new;
			new->next = ptr2;
			return (new);
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	/* if we reach the last node, meaning all the values of the */
	/* nodes are less than number, thus we append the new node. */
	ptr2->next = new;
	return (new);

}
