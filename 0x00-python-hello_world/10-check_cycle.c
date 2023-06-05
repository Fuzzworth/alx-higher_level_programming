#include "lists.h"

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
	size_t *seen_addresses = NULL, *temp_addresses = NULL;
	int count = 0;
	int i;

	while (list != NULL)
	{
		if (count > 0)
		{
			temp_addresses = malloc(sizeof(size_t) * (count + 1));
			if (temp_addresses == NULL)
				return (0);
			for (i = 0; i < count; i++)
				temp_addresses[i] = seen_addresses[i];
			free(seen_addresses);
			seen_addresses = NULL;
			for (i = 0; i < (count - 1); i++)
				if (temp_addresses[i] == (size_t) list)
					return (0);
		}
		count++;
		seen_addresses = malloc(sizeof(size_t) + (count + 1));
		if (seen_addresses == NULL)
			return (0);
		for (i = 0; i < (count - 1); i++)
			seen_addresses[i] = temp_addresses[i];
		seen_addresses[count - 1] = (size_t) list;
		list = list->next;
	}
	return (1);
}
