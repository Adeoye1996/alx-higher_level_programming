#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *current = *head, *next, *prev = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
    return *head;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *mid = NULL, *rev = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    if (fast)
        slow = slow->next;

    mid = slow;
    rev = reverse_listint(&mid);

    while (rev)
    {
        if ((*head)->n != rev->n)
        {
            reverse_listint(&mid);
            return 0;
        }
        *head = (*head)->next;
        rev = rev->next;
    }

    reverse_listint(&mid);
    return 1;
}
