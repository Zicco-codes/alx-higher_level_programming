#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


typedef struct listint {
	int n;
	struct listint *next;
} listint_t;

listint_t* reverse_list(listint_t *head) {
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL) {
		next = current->next;
		current->next = prev;
		rev = current;
		current = next;
	}

	return prev;
}


int is_palindrome(listint_t **head) {
	if (*head == NULL || (*head)->next == NULL) {
		return 1;
	}

	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = reverse_list(slow);
	fast = *head;

	while (slow != NULL) {
		if (slow->n != fast->n) {
			return 0;
		}
		slow = slow->next;
		fast = fast->next;
	}

	return 1;
}
