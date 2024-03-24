#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct listint_s {
 *     int n;
 *     struct listint_s *next;
 * };
 * typedef struct listint_s listint_t;
 */

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int size = 0, i = 0, j = 0;
    int *array = NULL;

    if (!head || !(*head) || !((*head)->next))
        return (1);

    while (current)
    {
        size++;
        current = current->next;
    }

    array = malloc(sizeof(int) * size);
    if (!array)
        return (0);

    current = *head;
    while (current)
    {
        array[i++] = current->n;
        current = current->next;
    }

    for (i = 0, j = size - 1; i < size / 2; i++, j--)
    {
        if (array[i] != array[j])
        {
            free(array);
            return (0);
        }
    }

    free(array);
    return (1);
}

