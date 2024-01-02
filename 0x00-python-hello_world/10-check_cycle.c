#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* Check if the list is NULL or has only one node (no cycle) */
	if (!list || !list->next)
		return (0);

	/* Traverse the list with slow and fast pointers */
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If there's a cycle, the pointers will meet */
		if (slow == fast)
			return (1);
	}

	/* If no cycle is found, return 0 */
	return (0);
}
