#include <stddef.h>
#include "lists.h"

/**
 * list_length - finds the length of a singly linked list.
 * @h: a pointer to the head of a listint_t list.
 * Return: the length of a singly linked list.
*/
unsigned int list_length(listint_t *h)
{
	listint_t *temp = h;
	unsigned int i = 0;

	while (temp->next != NULL)
	{
		i++;
		temp = temp->next;
	}
	return (i);
}


/**
 * list_sec_half - finds the second half of a singly linked list.
 * @head: a pointer to the head of a listint_t list.
 * Return: a pointer to the second half of listint_t singly linked list.
*/
listint_t *list_sec_half(listint_t *head)
{
	listint_t *first_half = head;
	listint_t *sec_half = NULL;
	unsigned int length = list_length(head);
	unsigned int first_half_len, i = 1;

	if (length % 2 != 0)
		first_half_len = length / 2 + 1;
	else
		first_half_len = length / 2;
	while (i <= first_half_len)
	{
		first_half = first_half->next;
		i++;
	}
	sec_half = first_half->next;
	first_half = NULL;
	return (sec_half);
}


/**
 * reverse_list - reverses a listint_t singly linked list.
 * @head: a pointer to the head of listint_t singly linked list.
 * Return: a pointer to the head of a reversed listint_t singly linked list.
*/
listint_t *reverse_list(listint_t *head)
{
	listint_t *reversed = head;
	listint_t *prev_node = NULL;
	listint_t *curr_node = head;
	listint_t *next_node = NULL;

	while (curr_node != NULL)
	{
		next_node = curr_node->next;
		curr_node->next = prev_node;
		prev_node = curr_node;
		curr_node = next_node;
	}
	reversed = prev_node;
	return (reversed);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to a pointer of listint_t singly linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *sec_half;
	listint_t *sec_reversed;
	int check = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (check);
	current = *head;
	sec_half = list_sec_half(current);
	sec_reversed = reverse_list(sec_half);
	while (sec_reversed->next != NULL)
	{
		if (sec_reversed->n != current->n)
		{
			check = 0;
			break;
		}
		sec_reversed = sec_reversed->next;
		current = current->next;
	}
	return (check);
}
