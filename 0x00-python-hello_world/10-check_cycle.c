#include <stdio.h>
#include "lists.h"

/**
 * print_seen - prints seen array
 *
 * Description: prints seen array
 *
 * @seen: seen array
 * @num: number of things to print
 *
 * Return: void
 */
void print_seen(size_t **seen, int num)
{
	int i;

	for (i = 0; i < num; i++)
		printf("\ncount = %d ,seen[%d] = %lu", num, i, *seen[i]);
}

/**
 * init_seen - prints seen array
 *
 * Description: prints seen array
 *
 * @seen: seen array
 * @list: list pointer
 * @count: number of things to print
 *
 * Return: void
 */
void init_seen(size_t **seen, listint_t **list, int *count)
{
	*seen = malloc(sizeof(size_t) * 1);
	if (*seen == NULL)
		exit(-1);
	(*seen)[0] = (size_t) *list;
	*count = *count + 1;
}

/**
 * has_been_seen - prints seen array
 *
 * Description: prints seen array
 *
 * @seen: seen array
 * @list: list pinter
 * @count: number of things to print
 *
 * Return: 1 for True, 0 for false
 */
int has_been_seen(size_t **seen, listint_t **list, int count)
{
	int i;

	for (i = 0; i < count - 1; i++)
		if ((*seen)[i] == ((size_t) *list))
			return (1);
	return (0);
}

/**
 * add_to_seen - prints seen array
 *
 * Description: prints seen array
 *
 * @seen: seen array
 * @list: list pointer
 * @num: number of things to print
 *
 * Return: void
 */
void add_to_seen(size_t **seen, listint_t **list, int *count)
{
	size_t *new_seen;
	int i;

	*count = *count + 1;
	new_seen = malloc(sizeof(size_t) * (*count));
	if (new_seen == NULL)
		exit(-1);
	for (i = 0; i < *count - 1; i++)
		new_seen[i] = (*seen)[i];
	new_seen[*count - 1] = (size_t) (*list);
	free(*seen);
	*seen = new_seen;
}

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 *
 * Description: function in C that checks if a singly linked list has a cycle
 * in it.
 *
 * @list: pointer to head
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	size_t *seen = NULL;
	int count = 0;

	while (list != NULL)
	{
		if (count == 0)
		{
			init_seen(&seen, &list, &count);
		}
		else
		{
			if (has_been_seen(&seen, &list, count))
			{
				free(seen);
				return (0);
			}
			add_to_seen(&seen, &list, &count);
		}
		list = list->next;
	}
	if (count > 0)
		free(seen);
	return (1);
}
