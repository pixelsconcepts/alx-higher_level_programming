#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Function to check
 * @PyObject: Parameter 1
 * @p: Parameter 2
 *
 * return: nothing
 */

void print_python_list_info(PyObject *p)
{
	int size, i;
	PyObject *item;
	
	size = PyList_Size(p);
	
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

