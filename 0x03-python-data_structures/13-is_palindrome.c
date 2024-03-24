#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int values[1000]; // Assuming a maximum of 1000 elements in the list
    int count = 0, i;

    // Store the values in the array
    while (current != NULL)
    {
        values[count++] = current->n;
        current = current->next;
    }

    // Check if the array is a palindrome
    for (i = 0; i < count / 2; i++)
    {
        if (values[i] != values[count - i - 1])
            return 0; // Not a palindrome
    }

    return 1; // Palindrome
}
