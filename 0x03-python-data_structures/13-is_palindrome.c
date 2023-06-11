#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 *
 * Description: function in C that checks if a singly linked list is a
 * palindrome.
 *
 * @head: Pointer to head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i, count = 0;
	int *list_array;

	while (current)
	{
		count++;
		current = current->next;
	}
	if (count == 0)
		return (0);
	current = *head;
	list_array = (int *) malloc(sizeof(int) * count);
	if (list_array == NULL)
		return (0);
	for (i = 0; i < ((count) / 2) && current != NULL; i++)
	{
		list_array[i] = current->n;
		current = current->next;
	}
	for (; i >= 0 && current != NULL; i--)
	{
		if (list_array[i] != current->n)
			return (0);
		current = current->next;
	}

	if (i != 0)
		return (0);

	return (1);
}
