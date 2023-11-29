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
 * add_node_beginning - add node at the beginning.
 * @head: pointer to pointer of first node of listint_t list.
 * @new_node: new node to add.
*/
void add_node_beginning(listint_t **head, listint_t *new_node)
{
	new_node->next = *head;
	*head = new_node;

}

/**
 * add_node_middle - add node at the middle.
 * @ptr1: first pointer to a node.
 * @ptr2: second pointer to a node.
 * @new_node: new node to add.
*/
void add_node_middle(listint_t *ptr1, listint_t *ptr2, listint_t *new_node)
{
	ptr1->next = new_node;
	new_node->next = ptr2;
}

/**
 * add_node_last - add a node at the end.
 * @last_node: pointer to the last node.
 * @new_node: new node to add.
*/
void add_node_last(listint_t *last_node, listint_t *new_node)
{
	if (last_node->next == NULL)
		last_node->next = new_node;
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
	if (new->n < (*head)->n)
		add_node_beginning(head, new);
	ptr1 = *head;
	ptr2 = (*head)->next;
	while (ptr2->next != NULL)
	{
		if (ptr2->n > new->n || ptr2->n > new->n)
		{
			add_node_middle(ptr1, ptr2, new);
			return (new);
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	/* if we reach the last node, meaning all the values of the */
	/* nodes are less than number, thus we append the new node. */
	add_node_last(ptr2, new);
	return (new);
}
