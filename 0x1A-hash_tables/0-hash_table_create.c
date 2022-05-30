#include "hash_tables.h"

/**
 * hash_table_create - function that creates a hash table
 *
 * @size: Is the size of the array
 * Return: pointer
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *array = NULL;

	array = (hash_table_t *)malloc(sizeof(hash_table_t) * size);
	if (array == NULL)
	{
		return (NULL);
	}
	return (array);
}
