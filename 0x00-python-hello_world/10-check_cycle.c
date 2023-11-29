#include "lists.h"
/** check_cycle -
  * @list:
  * Return:
  */
int check_cycle(listint_t *list)
{
	listint_t *slow_iterator, *fast_iterator;

	if (!list || !list->next)
		return (0);

	slow_iterator = list;
	fast_iterator = list;

	while (slow_iterator != NULL && fast_iterator != NULL)
	{
		slow_iterator = slow_iterator->next;
		fast_iterator = fast_iterator->next->next;

		if (slow_iterator == fast_iterator)
			return (1);
	}
	return (0);
}
